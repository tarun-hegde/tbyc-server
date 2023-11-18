from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class NewUser(AbstractUser):
    # email=models.EmailField(max_length=100,unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)  # Add the otp field here
    


    