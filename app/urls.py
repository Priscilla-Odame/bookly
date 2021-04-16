from django.conf.urls import url
from django.urls import path, include
from app.views.user import SignUpAPI, LoginView
from app.views.books import BookViews, books
from app.views.category import CategoryView
from app.views.borrow import OrderBookViewSet, dashboard, borrow
from rest_framework import routers
from app.views.user import login, register
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register(r'signup',SignUpAPI, 'signup')
router.register(r'login', LoginView, 'login-api')
router.register(r'books', BookViews, 'books')
router.register(r'category',CategoryView, 'category' )
router.register(r'borrow',OrderBookViewSet,'borrow')
# urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^books/', books, name='allbooks'),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^borrow/', borrow, name='borrow-book'),
    # path('api/login', LoginAPI.as_view(), name ='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)