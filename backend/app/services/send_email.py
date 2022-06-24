from django.core.mail.message import EmailMessage
from django.template.loader import get_template

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os


class Services:

    @staticmethod
    def send_email_with_embeded_images(ctx):
        # loading images to be embedded as bytes
        logo_png = open('./templates/icons/logo.png', 'rb').read()
        user_png = open('./templates/icons/user.png', 'rb').read()
        linkedin_png = open('./templates/icons/linkedin.png', 'rb').read()
        facebook_png = open('./templates/icons/facebook.png', 'rb').read()
        twitter_png = open('./templates/icons/twitter.png', 'rb').read()
        globe_png = open('./templates/icons/globe.png', 'rb').read()
        padlock_png = open('./templates/icons/padlock.png', 'rb').read()
        exclamation_png = open(
            './templates/icons/exclamation.png', 'rb').read()

        # indicating that images are part of the html message, not alternatives
        html_part = MIMEMultipart(_subtype='related')
        body = MIMEText(get_template(f"{ctx['template_name']}").render(ctx))
        html_part.attach(body)

        # attaching the images
        logo_image = MIMEImage(logo_png, 'png')
        logo_image.add_header('Content-Id', '<logo_png>')
        logo_image.add_header('Content-Disposition', 'inline', filename='logo')
        html_part.attach(logo_image)

        user_image = MIMEImage(user_png, 'png')
        logo_image.add_header('Content-Id', '<user>')
        logo_image.add_header('Content-Disposition', 'inline', filename='user')
        html_part.attach(user_image)

        linkedin_image = MIMEImage(linkedin_png, 'png')
        logo_image.add_header('Content-Id', '<linkedin>')
        logo_image.add_header('Content-Disposition',
                              'inline', filename='linkedin')
        html_part.attach(linkedin_image)

        facebook_image = MIMEImage(facebook_png, 'facebook')
        logo_image.add_header('Content-Id', '<logo_png>')
        logo_image.add_header('Content-Disposition',
                              'inline', filename='facebook')
        html_part.attach(facebook_image)

        twitter_image = MIMEImage(twitter_png, 'png')
        logo_image.add_header('Content-Id', '<twitter>')
        logo_image.add_header('Content-Disposition',
                              'inline', filename='twitter')
        html_part.attach(twitter_image)

        globe_image = MIMEImage(globe_png, 'png')
        logo_image.add_header('Content-Id', '<globe>')
        logo_image.add_header('Content-Disposition',
                              'inline', filename='globe')
        html_part.attach(globe_image)

        padlock_image = MIMEImage(padlock_png, 'png')
        logo_image.add_header('Content-Id', '<padlock>')
        logo_image.add_header('Content-Disposition',
                              'inline', filename='padlock')
        html_part.attach(padlock_image)

        exclamation_image = MIMEImage(exclamation_png, 'png')
        logo_image.add_header('Content-Id', '<exclamation>')
        logo_image.add_header('Content-Disposition',
                              'inline', filename='exclamation')
        html_part.attach(exclamation_image)

        content = EmailMessage(
            ctx["subject"],
            None,
            # os.environ.get("EMAIL_HOST_USER"),
            ctx["recipients"],
        )
        content.attach(html_part)
        content.send()
