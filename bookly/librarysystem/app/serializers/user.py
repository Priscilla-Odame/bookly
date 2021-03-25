from rest_framework import serializers
from app.models import User
from rest_framework.exceptions import AuthenticationFailed
from app.utils import token_generator
from django.contrib.auth import authenticate, get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):  

    class Meta:
        model = User
        fields = ('firstname', 'lastname','email','password','date_of_birth')
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):  
        User = get_user_model()
        user = User.objects.create_user(
            validated_data['firstname'],
            validated_data['lastname'],
            validated_data['email'],
            validated_data['date_of_birth'],
            validated_data['password'])
        return user

    # def validate(self, attrs):
    #     attrs = super().validate(attrs)
    #     user = User.objects.create_user(**attrs)
    #     user.save()
    #     return attrs

class LogInSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField(max_length=225)

    class Meta:
        model = User
        fields = ('firstname', 'lastname','email','password','date_of_birth','tokens')
        extra_kwargs = {
            'password': {'write_only': True},
            'firstname': {'read_only': True},
            'lastname': {'read_only': True},
            'date_of_birth':{'read_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        print(f'---------------{email}')
        print(f'---------------{password}')

        user = authenticate(email=email, password=password)
        print(f'---------------{user}')
        if not user:
            raise AuthenticationFailed('Invalid Credential. Try again')

        return {
            'firstname': user.firstname,
            'email': user.email,
            'lastname': user.lastname,
            'tokens': user.tokens
        }
