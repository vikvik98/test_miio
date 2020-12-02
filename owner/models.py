from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Owner(models.Model):
    user_django = models.OneToOneField(User, related_name="owner", on_delete=models.PROTECT, unique=True)
    name = models.CharField("Full name", max_length=180)
