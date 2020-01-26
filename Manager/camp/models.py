from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class CampData(models.Model):
    rule_name = models.CharField(max_length = 50)
    campaigns = models.CharField(max_length = 50)
    schedule_start = models.DateTimeField()
    schedule_stop = models.DateTimeField()
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    spend = models.IntegerField()
    eCPM = models.IntegerField()
    eCPC = models.IntegerField()
    installs = models.IntegerField()
    eCPI = models.IntegerField()
    action = models.CharField(max_length = 20)
    status = models.BooleanField(default = True)

    def __str__(self):
        return self.rule_name
