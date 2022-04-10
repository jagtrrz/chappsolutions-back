from rest_framework.routers import DefaultRouter

from app.bookings.views import BookingsViewSet
from app.rooms.views import RoomsViewSet, RoomsAvailableViewSet

router = DefaultRouter()

router.register(r'bookings', BookingsViewSet)
router.register(r'rooms', RoomsViewSet)
router.register(r'rooms-available', RoomsAvailableViewSet)

urlpatterns = router.urls