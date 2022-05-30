from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Booking, Process_booking, Constituency, Ward

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class BookingProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process_booking
        fields = "__all__"

class ConstituencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ConstituencySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WardSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            self.Meta.depth = 1