import holidays
from django.http import request
from django.shortcuts import render
from ics import Calendar, Event
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView

from app_calendar.models import Holiday, Country
from app_calendar.serializer import CountrySerializer, EventSerializer, UserSerializer, \
    HolidaySerializerRead, HolidaySerializerWrite


class ListCountries(ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        if self.kwargs.get('name'):
            return Country.objects.filter(name=self.kwargs.get('name'))
        return Country.objects.all()


class ListHolidays(ListAPIView):
    serializer_class = HolidaySerializerRead

    def get_queryset(self):
        # if self.kwargs.get('id'):
        #     return Holiday.objects.filter(id=self.kwargs.get('id'))
        return Holiday.objects.all()


class ListCountryHolidays(ListAPIView):
    serializer_class = HolidaySerializerRead

    def get_queryset(self):
        if self.kwargs.get('id'):
            return Holiday.objects.filter(country=self.kwargs.get('id'))
        return Holiday.objects.all()


class CreateHolidays(CreateAPIView):
    serializer_class = HolidaySerializerWrite