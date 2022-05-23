from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

# Create your models here.
class Profile(TrackingModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ward = models.CharField(max_length=150, blank=True)
    building = models.CharField(max_length=150, blank=True)
    hse_no = models.CharField(max_length=100, blank=True)
    national_id = models.CharField(max_length=100, blank=True)
    attachment = models.ImageField(upload_to='attachments/', default='default.jpg')

    def __str__(self) -> str:
        return self.user.username
