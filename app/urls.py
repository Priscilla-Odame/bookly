from django.conf.urls import url
from django.urls import path, include
from app.views.user import SignUpAPI, LoginView
from app.views.books import BookViews, books, CountAPI
from app.views.category import CategoryView
from app.views.borrow import BorrowBookViewSet, dashboard, borrow, admindashboard, CountBorrowAPI
from app.views.password_reset import SetNewPasswordAPI
from rest_framework import routers
from app.views.user import login, register
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register(r'signup',SignUpAPI, 'signup')
router.register(r'login', LoginView, 'login-api')
router.register(r'books', BookViews, 'books')
router.register(r'category',CategoryView, 'category' )
router.register(r'borrow',BorrowBookViewSet,'borrow')
router.register(r'password',SetNewPasswordAPI,'password-reset')
# router.register(r'countborrow', CountBorrowViewSet,'')
# urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^books/', books, name='allbooks'),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^admindash/', admindashboard, name='admin-dashboard'),
    url(r'^borrow/', borrow, name='borrow-book'),
    path('api/count', CountAPI.as_view(), name ='count'),
    path('api/countborrow', CountBorrowAPI.as_view(), name ='countborrow'),
    # path('api/login', LoginAPI.as_view(), name ='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)