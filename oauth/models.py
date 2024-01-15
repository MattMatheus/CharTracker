from django.db import models


# Create your models here.
class UserAuthDetails(models.Model):
    scope = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    sub = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
