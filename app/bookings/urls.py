from rest_framework.routers import DefaultRouter

from app.bookings.views import BookingsViewSet

router = DefaultRouter()

router.register(r'', BookingsViewSet)

urlpatterns = router.urls
