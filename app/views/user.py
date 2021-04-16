from django.shortcuts import render, redirect
from rest_framework import viewsets
from app.models import User
from rest_framework import generics,status, permissions
from app.serializers.user import SignUpSerializer, LogInSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import HttpResponse


# Create your views here.
class SignUpAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = SignUpSerializer
    queryset = User.objects

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            return Response({
                "user": SignUpSerializer(user,
                context=self.get_serializer_context()).data
            })
        return Response

class LoginView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = LogInSerializer
    queryset = User.objects
    http_method_names = ['get','post', 'head']
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def register(request):
    return render(request,'signup.html')

def login(request):
        return render(request,'login.html')

