from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from app.models.user import User
from app.models.company import Company
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework.reverse import reverse
from app.utils import token_generator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['firstname', 'othernames', 'email', 'company', 'password']

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = User.objects.create_user(**attrs)
        user.save()
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=225)

    class Meta:
        model = User
        fields = ('id', 'firstname', 'othernames',
                  'email', 'company', 'password', 'tokens')
        extra_kwargs = {
            'password': {'write_only': True},
            'style': {'input_type': 'password'},
            'firstname': {'read_only': True},
            'othernames': {'read_only': True},
            'company': {'read_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credential. Try again')

        return {
            'id': user.id,
            'firstname': user.firstname,
            'email': user.email,
            'othernames': user.othernames,
            'company': user.company,
            'tokens': user.tokens
        }


class ValidateEmailSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(max_length=225)

    class Meta:
        model = User
        fields = ('email',)


class ActivateDeactivateUserAccount(serializers.Serializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)
        errors = []
        try:
            uid = urlsafe_base64_decode(attrs['uidb64']).decode()
            user = User.objects.get(pk=uid)
            if not token_generator.check_token(user, attrs['token']):
                errors.append("User email already verified")
            if user.is_active:
                errors.append("User account already activated")

        except Exception as ex:
            errors.append(ex)
            raise ex
        if errors:
            return {'messages': errors}
        user.is_active = True
        user.save()
        return {"success": reverse("login")}


class ListAllCompanyMembersSerializer(serializers.ModelSerializer):

    def get_company_staff(self, attrs):
        company = Company.objects.get(pk=attrs['company_id'])
        company_id = company.id
        company_name = company.name
        company_members = User.objects.values(
            'firstname',
            'othernames',
            'email',
            'id',
        ).filter(company=company_id)

        return {'company': company_name, "staff": company_members}
