from django.contrib import admin
from .models import User, vehicle_details

# Register your models here.

admin.site.register(User)
admin.site.register(vehicle_details)
