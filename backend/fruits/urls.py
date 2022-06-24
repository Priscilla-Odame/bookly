from rest_framework import routers
from fruits.views import FruitViewSet

router = routers.DefaultRouter()
router.register(r'', FruitViewSet, basename='fruits')
urlpatterns = router.urls