from django.db import models
from helpers.models import TrackingModel

# Create your models here.
class Agent(TrackingModel):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=10)
    age = models.SmallIntegerField()
    residence = models.CharField(max_length=200)
    next_kin = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name
