from rest_framework.routers import DefaultRouter

from app.rooms.views import RoomsViewSet

router = DefaultRouter()

router.register(r'', RoomsViewSet)

urlpatterns = router.urls
