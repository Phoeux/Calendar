from django.contrib import admin

from app_calendar.models import Event, User, Country, Holiday

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Country)
admin.site.register(Holiday)
# Register your models here.
