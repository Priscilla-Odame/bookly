from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User
from .serializers import LogInSerializer
from rest_framework.response import Response


# Create your views here.

class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = LogInSerializer
    queryset = User.objects
    http_method_names = ['get','post', 'head']

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
