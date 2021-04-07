from django.conf.urls import url
from django.urls import path, include
from app.views.user import SignUpAPI, LoginView
from app.views.books import BookViews, books
from app.views.category import CategoryView
from app.views.borrow import OrderBookViewSet
from rest_framework import routers
from app.views.user import logins, register

router = routers.DefaultRouter()

router.register(r'signup',SignUpAPI, 'signup')
router.register(r'login', LoginView, 'login')
router.register(r'books', BookViews, 'books')
router.register(r'category',CategoryView, 'category' )
router.register(r'borrow',OrderBookViewSet,'borrow')
# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    url(r'^logins/', logins, name='logins'),
    url(r'^register/', register, name='register'),
    url(r'^bookss/', books, name='bookss'),
    # path('api/login', LoginAPI.as_view(), name ='login')
]