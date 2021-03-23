from rest_framework import serializers
from app.models import User
from rest_framework.exceptions import AuthenticationFailed
from app.utils import token_generator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):  

    class Meta:
        model = User
        fields = ('firstname', 'lastname','email','password','username','date_of_birth')
        extra_kwargs = {'password': {'write_only' : True}}

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = User.objects.create_user(**attrs)
        user.save()
        return attrs

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=225)

    class Meta:
        model = User
        fields = ('firstname', 'lastname','email','password','username','date_of_birth','token')
        extra_kwargs = {
            'password': {'write_only': True},
            'firstname': {'read_only': True},
            'lastname': {'read_only': True},
            'username': {'read_only': True},
            'date_of_birth':{'read_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credential. Try again')

        return {
            'firstname': user.firstname,
            'email': user.email,
            'othernames': user.othernames,
            'company': user.company,
            'tokens': user.tokens
        }
