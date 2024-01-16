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
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.char_name


class QuestCompletionStatus(models.Model):
    quest_id = models.IntegerField()
    name = models.CharField(max_length=64)
    data_link = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quest_name
