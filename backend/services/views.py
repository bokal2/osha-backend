from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer, BookingProcessSerializer
from .models import Booking, Process_booking

# Create your views here.
class BookingAPIView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated,)

class ProcessBookingView(viewsets.ModelViewSet):
    serializer_class = BookingProcessSerializer
    queryset = Process_booking.objects.all()
    permission_classes = (IsAuthenticated,)