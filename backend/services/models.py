from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

# Create your models here.

class Booking(TrackingModel):
    ROOMS = [
        ("SINGLE_ROOM", "Single Room"),
        ("BEDSITTER", "Bedsitter"),
        ("ONE_BEDROOM", "One Bedroom"),
        ("TWO_BEDROOM", "Two Bedroom"),
        ("THREE_BEDROOM", "Three Bedroom"),
        ("FOUR_BEDROOM", "Four Bedroom"),
        ("MORE", "More than 4"),
    ]

    home_size = models.CharField(choices=ROOMS, default="ONE_BEDROOM", max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    services = models.JSONField(default=dict)
    quantity = models.IntegerField(default=0)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service_fee = models.FloatField()
    paid = models.BooleanField(default=False)
    express = models.BooleanField(default=False)

    def __str__(self) -> str:
        return " {0} - Booking - {1}".format(self.client.full_name, self.created_at)

class Process_booking(TrackingModel):
    STATUSES = [
        ("INPROGRESS", "InProgress"),
        ("COMPLETE", "Complete"),
        ("CANCELLED", "Cancelled")
    ]
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    status = models.CharField(choices=STATUSES, default="COMPLETE", max_length=100)
    comments = models.TextField()

    def __str__(self) -> str:
        return "Processed booking on - {0}".format(self.created_at)

class Constituency(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
class Ward(models.Model):
    constituency_name = models.ForeignKey(Constituency, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name