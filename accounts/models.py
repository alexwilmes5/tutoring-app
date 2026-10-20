from django.contrib.auth.models import AbstractUser
from django.db import models

# Fields for user
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    course = models.CharField(max_length=100)
    name = models.CharField(null = True, max_length=100)
    hours = models.CharField(null = True, max_length=100)
    day = models.CharField(null = True, max_length=100)