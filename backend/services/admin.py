from django.contrib import admin
from .models import Booking, Process_booking, Ward, Constituency

# Register your models here.
admin.site.register(Booking)
admin.site.register(Process_booking)
admin.site.register(Constituency)
admin.site.register(Ward)
