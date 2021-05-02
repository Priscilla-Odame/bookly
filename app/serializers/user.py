from rest_framework import serializers
from app.models import User
from rest_framework.exceptions import AuthenticationFailed
from app.utils import token_generator
from django.contrib.auth import authenticate, get_user_model
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):  

    class Meta:
        model = User
        fields = ('id','firstname', 'lastname','email','password','date_of_birth')
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

class LogInSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    firstname = serializers.CharField(read_only= True, max_length=100)
    lastname = serializers.CharField(read_only= True, max_length=100)
    date_of_birth = serializers.DateField(read_only=True, default=date.today)
    access_token = serializers.ReadOnlyField(source='user_access_token')
    refresh_token = serializers.ReadOnlyField(source='user_refresh_token')
    

    # class Meta:
    #     model = User
    #     fields = ('firstname', 'lastname','email','password','date_of_birth','tokens')
    #     extra_kwargs = {
    #         'password': {'write_only': True},
    #         'firstname': {'read_only': True},
    #         'lastname': {'read_only': True},
    #         'date_of_birth':{'read_only': True}
    #     }

    def create(self, validated_data):
        return validated_data

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credential. Try again')

        return {
            'id':user.id,
            'firstname': user.firstname,
            'email': user.email,
            'lastname': user.lastname,
            'date_of_birth': user.date_of_birth,
            'user_access_token': user.get_access_token,
            'user_refresh_token': user.get_refresh_token        
        }

    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     password = attrs.get('password', '')

    #     print(f'---------------{email}')
    #     print(f'---------------{password}')

    #     user = authenticate(email=email, password=password)
    #     print(f'---------------{user}')
    #     if not user:
    #         raise AuthenticationFailed('Invalid Credential. Try again')

    #     return {
    #         'firstname': user.firstname,
    #         'email': user.email,
    #         'lastname': user.lastname,
    #         'date_of_birth': user.date_of_birth,
    #         'user_access_token': user.get_access_token,
    #         'user_refresh_token': user.get_refresh_token        
    #     }
