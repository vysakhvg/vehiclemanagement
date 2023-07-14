from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    user_type = models.CharField(max_length=250)


vehicle_choices = (('2-wheeler', 'Two-wheeler'), ('3-wheeler', 'Three-wheeler'), ('4-wheeler', 'Four-wheeler'))


class vehicle_details(models.Model):
    vehicle_number = models.CharField(max_length=250)
    vehicle_type = models.CharField(max_length=250, choices=vehicle_choices, default='2-wheeler')
    vehicle_model = models.CharField(max_length=250)
    vehicle_description = models.TextField()
