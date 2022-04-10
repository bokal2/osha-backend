from django.db import models
from helpers.models import TrackingModel

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

    home_size = models.CharField(choices=ROOMS, default="ONE_BEDROOM", max_length=255)
    booking_date = models.DateFied()
    booking_time = models.TimeField()
    services = models.JSONField(default=dict)
    quantity = models.IntegerField(default=0)



