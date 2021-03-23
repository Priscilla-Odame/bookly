from django.urls import path
from app.views.user import SignUpAPI
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'signup',SignUpAPI, 'signup')
urlpatterns = router.urls