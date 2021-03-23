from django.shortcuts import render
from rest_framework import viewsets
from app.models import User
from rest_framework import generics,status
from app.serializers.user import SignUpSerializer
from rest_framework.response import Response

# Create your views here.
class SignUpAPI(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer
    queryset = User.objects

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     email = serializer.validated_data.get('email', '')

    #     return Response(serializer.data, status.HTTP_201_CREATED)