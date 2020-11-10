from calendar import calendar

from django.contrib.auth.models import AbstractUser
from django.db import models


# class Year(models.Model):
#     year = models.PositiveIntegerField(default=0)
class Country(models.Model):
    name = models.CharField(max_length=20)


class User(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)


class Holiday(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    location = models.CharField(max_length=20)
    description = models.TextField()


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE)
    timedelta = models.DurationField()
    need_remind = models.BooleanField()

# class Reminder(models.Model):
#     text = models.CharField(max_length=100)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)

# Create your models here.
