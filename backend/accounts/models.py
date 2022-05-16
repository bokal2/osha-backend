from django.db import models
from helpers.models import TrackingModel
from authentication.models import User

# Create your models here.
class Profile(TrackingModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ward = models.CharField(max_length=150, blank=True)
    building = models.CharField(max_length=150, blank=True)
    hse_no = models.CharField(max_length=100, blank=True)
    national_id = models.CharField(max_length=100, blank=True)
    # attachment = models.FileField(upload_to='attachments/', blank=False, null=False)

    def __str__(self) -> str:
        return self.user.full_name
