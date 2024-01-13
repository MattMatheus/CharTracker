from django.db import models


# Create your models here.
class UserAuthDetails(models.Model):
    scope = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
