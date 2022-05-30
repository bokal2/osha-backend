from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentApiView

app_name = "agents_api"

router = DefaultRouter()
router.register("", AgentApiView, basename="agents")

urlpatterns = [
    path("", include(router.urls)),
]
