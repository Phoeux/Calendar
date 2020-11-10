from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from app_calendar.models import Event, Holiday, Country, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class HolidaySerializer(ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
