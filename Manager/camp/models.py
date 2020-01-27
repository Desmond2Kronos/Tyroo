from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

class CampData(models.Model):
    rule_name = models.CharField(max_length = 50)
    campaigns = models.CharField(max_length = 50)
    schedule_start = models.DateTimeField(auto_now_add=True, blank=True)
    schedule_stop = models.DateTimeField(auto_now_add=True, blank=True)
    impressions = models.IntegerField(default=0, blank=True)
    clicks = models.IntegerField(default=0, blank=True)
    spend = models.IntegerField(default=0, blank=True)
    eCPM = models.IntegerField(default=0, blank=True)
    eCPC = models.IntegerField(default=0, blank=True)
    installs = models.IntegerField(default=0, blank=True)
    eCPI = models.IntegerField(default=0, blank=True)
    status = models.BooleanField(default=True, blank = True)

    def __str__(self):
        return self.rule_name

class CampGatheredData(models.Model):
    campaign_name = models.CharField(max_length = 50)
    schedule_start = models.TimeField(auto_now=False, blank=True)
    schedule_stop = models.TimeField(auto_now=False, blank=True)
    impressions = models.IntegerField(default=0, blank=True)
    clicks = models.IntegerField(default=0, blank=True)
    spend = models.IntegerField(default=0, blank=True)
    installs = models.IntegerField(default=0, blank=True)
    status = models.BooleanField(default=True, blank = True)

    def __str__(self):
        return self.campaign_name
