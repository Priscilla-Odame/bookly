from rest_framework import serializers
from auths.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'groups': {'read_only' : True},'user_permissions': {'read_only' : True} }


class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=225)
    password = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    firstname = serializers.CharField(read_only= True, max_length=100)
    lastname = serializers.CharField(read_only= True, max_length=100)
    phone_number =serializers.CharField(read_only= True, max_length=100)
    access_token = serializers.ReadOnlyField(source='user_access_token')
    refresh_token = serializers.ReadOnlyField(source='user_refresh_token')
    

    # class Meta:
        # model = User
        # fields = ('firstname','lastname','email','password',)

        # extra_kwargs = {
        #     'password': {'write_only': True},
        #     'firstname': {'read_only': True},
        #     'lastname': {'read_only': True},
        #     'phone_number': {'read_only': True}
        # }
 
    def create(self, validated_data):
        return validated_data

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credential. Try again')

        return {
            'firstname': user.firstname,
            'email': user.email,
            'lastname': user.lastname,
            'phone_number': user.phone_number,
            'user_access_token': user.get_access_token,
            'user_refresh_token': user.get_refresh_token        
        }

