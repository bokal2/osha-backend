from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingAPIView, ProcessBookingView, WardAPIView, ConstituencyAPIView

app_name = "services_api"

router = DefaultRouter()
router.register("new-booking", BookingAPIView, basename="new-booking")
router.register("process-booking", ProcessBookingView, basename="process-booking")
router.register("constituency-list", ConstituencyAPIView, basename="constituency-list")
router.register("ward-list", WardAPIView, basename="ward-list")

urlpatterns = [
    path("", include(router.urls)),
]
