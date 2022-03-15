from email import message
from unicodedata import name
from django.db import models

# Create your models here.

class StartFriendShip(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    