from app.models.oauth_whitelist import CompaniesWhitelist
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.exceptions import AuthenticationFailed
from app.models.user import User
from app.models.company import Company
from app.utils import OAuth
import os
from app.serializers.company import CompanySerializer


class OAuthSerializer(serializers.Serializer):
    """Handles serialization of third party OAuth related data"""

    auth_token = serializers.CharField(write_only=True)
    auth_provider = serializers.CharField(write_only=True)

    def validate(self, attrs):
        auth_token = attrs.get('auth_token', '')
        auth_provider = attrs.get('auth_provider', '')

        user_data = OAuth.oauth_login(auth_token)

        try:
            email = user_data['mail']
            # user_domain = [email[email.index("@")+1:]]
            user_domain = [email.split("@")[-1]]

            user_company = OAuth.is_whitelisted(user_domain)

            name = f"{user_data['givenName']} {user_data['surname']}"

            user_email = OAuth.continue_with_oauth(
                provider=auth_provider,
                company=user_company,
                email=email,
                name=name
            )

            user = authenticate(
                email=user_email, password=os.environ.get('OAUTH_SECRET'))

            return {
                'id': user.id,
                'firstname': user.firstname,
                'othernames': user.othernames,
                'email': user.email,
                'company': user.company.id,
                'tokens': user.tokens()
            }
        except Exception as identifier:

            raise serializers.ValidationError(identifier)

class CompanyWhitelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaniesWhitelist
        fields = '__all__'