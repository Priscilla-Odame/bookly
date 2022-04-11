from django.urls import path, include
from app.views.user import LoginView, SignUpAPI
# from app.views.books import BookViews
# from app.views.category import CategoryView
# from app.views.purchase import OrderBookViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'api/signup',SignUpAPI, 'signup')
# router.register(r'api/login', LoginView, 'login')
# router.register(r'api/books', BookViews, 'books')
# router.register(r'api/category',CategoryView, 'category' )
# router.register(r'api/borrow',OrderBookViewSet,'borrow')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('api/login', LoginView.as_view(), name='login'),
]