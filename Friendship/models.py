from email import message
from django.db import models

# Create your models here.

class StartFriendShip(models.Model):
    name = models.CharField(max_length=50, blank='Rekruto')
    message = models.TextField(blank='Давай дружить')