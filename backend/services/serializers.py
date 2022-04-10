from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Booking, Process_booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class BookingProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process_booking
        fields = "__all__"