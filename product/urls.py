from rest_framework.routers import DefaultRouter

from product.views import SnackViewSet

router = DefaultRouter()

router.register("", SnackViewSet, basename="product")

urlpatterns = router.urls
