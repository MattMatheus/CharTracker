from django.db import models


# Create your models here.
class WeeklyCharProgress(models.Model):
    char_name = models.CharField(max_length=16)
    superbloom = models.BooleanField()
    rep_weekly = models.BooleanField()
    dream_seeds = models.BooleanField()

    def __str__(self):
        return self.char_name
