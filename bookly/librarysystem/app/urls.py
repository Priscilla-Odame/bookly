from django.urls import path, include
from app.views.user import SignUpAPI, LoginView
from app.views.books import BookViews
from app.views.category import CategoryView
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'signup',SignUpAPI, 'signup')
router.register(r'login', LoginView, 'login')
router.register(r'books', BookViews, 'books')
router.register(r'category',CategoryView, 'category' )
urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/login', LoginAPI.as_view(), name ='login')
# ]