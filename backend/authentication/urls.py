from django.urls import path
from .views import RegisterAPIView, LoginAPIView, AuthUserAPIView, VerifyEmail

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('user/', AuthUserAPIView.as_view(), name="user"),
]