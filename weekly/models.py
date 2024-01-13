from django.db import models


# Create your models here.
class WeeklyCharProgress(models.Model):
    char_name = models.CharField(max_length=16)
    superbloom = models.BooleanField()
    rep_weekly = models.BooleanField()
    dream_seeds = models.BooleanField()
    raidfinder_1 = models.BooleanField()
    raidfinder_2 = models.BooleanField()
    raidfinder_3 = models.BooleanField()
    raidfinder_4 = models.BooleanField()

    def __str__(self):
        return self.char_name


class UserAuthDetails:
    def __init__(self) -> None:
        pass
