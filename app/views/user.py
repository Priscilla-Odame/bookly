from django.shortcuts import render, redirect
from rest_framework import viewsets
from app.models import User
from rest_framework import generics,status, permissions
from app.serializers.user import SignUpSerializer, LogInSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate


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
        # return render(request,'login.html',serializer.data)

def register(request):
    # if request.method == 'POST':
    #     data = request.POST['firstname','lastname','email','date_of_birth','password']
    #     if data.is_valid():
    #         data.save()
    #         email = data.get('email')
    #         password = data.get('password')
    #         user = authenticate(email=email, password=raw_password)
    #         login(request, user)
    #         return redirect('home')
    return render(request,'signup.html')

def logins(request):
        # if request.method == 'POST':
        #     data = request.POST['email','password']
        return render(request,'login.html')

