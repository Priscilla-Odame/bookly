from django.core.mail import EmailMessage
from rest_framework.views import exception_handler
from django.contrib.auth import authenticate, get_user_model
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.reverse import reverse
from django.template.loader import get_template
import os
import requests
import json
from app.models.user import User
from app.models.company import Company
from app.models.oauth_whitelist import CompaniesWhitelist
from smtplib import SMTPException
from asgiref.sync import sync_to_async
import asyncio


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active) + text_type(user.pk) + text_type(timestamp))


token_generator = AppTokenGenerator()


class Utils:
    @staticmethod
    async def send_report_email(ctx):
        """utility service to handle report upload details email """

        message = get_template('mail.html').render(ctx)
        msg = EmailMessage(
            ctx["subject"],
            message,
            os.environ.get("EMAIL_HOST_USER"),
            [ctx["recepient"]],
        )
        msg.content_subtype = "html"
        # Main content is now text/html
        A_send = sync_to_async(msg.send, thread_sensitive=False)
        await A_send()

    @staticmethod
    async def send_email_verification_mail(user, domain):
        """utility service to handle user email verificaion"""

        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        link = reverse("verify_email",
                       kwargs={
                           "uidb64": uidb64,
                           "token": token_generator.make_token(user)
                       })
        verificationUrl = f"http://{domain}{link}"
        ctx = {
            "firstname": user.firstname,
            "activationLink": verificationUrl
        }
        message = get_template("verify_mail.html").render(ctx)
        email_subject = "Email Verification"
        email = EmailMessage(
            email_subject,
            message,
            os.environ.get("EMAIL_HOST_USER"),
            [user.email],
        )
        email.content_subtype = "html"
        # Main content is now text/html
        await sync_to_async(email.send, thread_sensitive=True)(fail_silently=False)

    async def send_invitation_mail(invitees, domain, sender, invitee_id_queryset, name):
        """utility service to handle user email invitaion"""

        uidb64 = urlsafe_base64_encode(force_bytes(invitees))
        token = PasswordResetTokenGenerator().make_token(invitee_id_queryset)
        ids = invitee_id_queryset.id
        A_reverse = sync_to_aync(reverse)
        link = await A_reverse("acceptinvite",
                               kwargs={
                                   'id': ids,
                                   "uidb64": uidb64,
                                   "token": token
                               })
        invitationUrl = f"http://{domain}{link}"
        ctx = {
            "firstname": invitee_id_queryset.firstname,
            "senderfirstname": sender.firstname,
            "senderothername": sender.othernames,
            "name": name,
            "company_name": sender.company,
            "invitationLink": invitationUrl
        }
        message = get_template("email.html").render(ctx)
        email_subject = "Invitation to join Project " + str(name)
        msgs = EmailMessage(
            email_subject,
            message,
            os.environ.get("EMAIL_HOST_USER"),
            [invitee_id_queryset]
        )
        msgs.content_subtype = "html"
        A_send = sync_to_async(msgs.send, thread_sensitive=False)
        await A_send()

    def custom_exception_handler(exc, context):
        # Call REST framework's default exception handler first,
        # to get the standard error response.
        response = exception_handler(exc, context)

        # Now add the HTTP status code to the response.
        if response is not None:
            response.data['status_code'] = response.status_code
            response.data['details'] = response.details

        return response

    def create_path(instance, filename):
        user = instance.user
        company_name = user.company
        file_path = f"{company_name}/{instance.project}/{filename}"
        return file_path

    def create_company_file_upload_path(instance, filename):
        user = instance.user
        company_name = user.company
        file_path = f"{company_name}/{user.pk}/{filename}"

        return file_path

    def create_directory_path(instance, filename):
        user = instance.user
        company_name = user.company
        directory_path = f"{company_name}/{user.pk}/{instance.directory}/{filename}"

        return directory_path

    async def send_password_reset_email(email, current_site):

        try:
            user = await sync_to_async(User.objects.get)(email=email)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)

            reset_password_url = f"http://{current_site}/auth/reset_password?uidb64={uidb64}&token={token}"

            ctx = {
                "firstname": user.firstname,
                "PasswordResetLink": reset_password_url,
                "uidb64": uidb64,
                "token": token
            }
            message = get_template("password_reset_email.html").render(ctx)
            email = EmailMessage(
                "Password Reset",
                message,
                os.environ.get("EMAIL_HOST_USER"),
                [user.email],
            )

            email.content_subtype = "html"
            A_send_mail = sync_to_async(email.send, thread_sensitive=False)
            await A_send_mail(fail_silently=False)

        except SMTPException as e:
            print('There was an error sending the password reset email.' + e)
        except Exception as ee:
            print('There was an error sending the password reset email.' + ee)


class OAuth:

    def is_whitelisted(user_domain):

        whitelisted = CompaniesWhitelist.objects.filter(
            domain_names__contains=user_domain)

        if whitelisted.exists():
            if len(whitelisted) > 1:
                raise ValidationError(
                    "User domain found in multiple whitlist, contact admin")
            else:

                return whitelisted[0].company

        else:

            raise ValidationError(
                "User's domain not found in domains whitelist")

    def oauth_login(auth_token):

        url = "https://graph.microsoft.com/v1.0/me"

        try:
            profile = requests.get(
                url, headers={'Authorization': 'Bearer ' + auth_token})

            return json.loads(profile.text)
        except Exception as e:
            print(f"Microsoft OAuth login error: {e}")
            return "The token is invalid or expired."

    def continue_with_oauth(provider, company, email, name):

        filtered_user_by_email = User.objects.filter(email=email)

        if filtered_user_by_email.exists():

            if provider == filtered_user_by_email[0].auth_provider:

                registered_user = authenticate(
                    email=email, password=os.environ.get('OAUTH_SECRET'))

                return registered_user

            else:
                raise AuthenticationFailed(
                    detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        else:
            user_data = {
                'email': email,
                'firstname': name.split()[0],
                'othernames': name[name.find(' '):],
                'company': company}
            user = User.objects.create_user(**user_data)
            user.set_password(os.environ.get('OAUTH_SECRET'))
            user.is_verified = True
            user.is_active = True
            user.auth_provider = provider
            user.save()

            return user.email
