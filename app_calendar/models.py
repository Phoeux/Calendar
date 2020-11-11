from calendar import calendar

from django.contrib.auth.models import AbstractUser
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Holiday(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    timedelta = models.DurationField()
    need_remind = models.BooleanField()

