from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileAPIView

app_name = "accounts_api"

router = DefaultRouter()
router.register("", ProfileAPIView, basename="accounts")

urlpatterns = [
    path("", include(router.urls)),
]
