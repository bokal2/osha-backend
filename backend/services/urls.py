from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingAPIView, ProcessBookingView

app_name = "services_api"

router = DefaultRouter()
router.register("", BookingAPIView, basename="services")
router.register("process-services", BookingAPIView, basename="process-services")

urlpatterns = [
    path("", include(router.urls)),
]
