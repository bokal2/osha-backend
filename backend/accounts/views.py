from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.
class ProfileAPIView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = "user"
    permission_classes = (IsAuthenticated,)

