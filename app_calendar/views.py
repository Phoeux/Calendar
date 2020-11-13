import django_filters
import holidays
from django.http import request
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, BaseInFilter, CharFilter, RangeFilter
from ics import Calendar, Event
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from app_calendar.models import Holiday, Country
from app_calendar.serializer import CountrySerializer, EventSerializer, UserSerializer, \
    HolidaySerializerRead, HolidaySerializerWrite


class ListCountries(ListAPIView):
    serializer_class = CountrySerializer
    # queryset = Country.objects.all()
    # filter_backends = (DjangoFilterBackend)
    # filter_fields = ['name']

    def get_queryset(self):
        # if self.kwargs.get('name'):
        #     return Country.objects.filter(name=self.kwargs.get('name'))
        return Country.objects.all()


class CountryViewSet(ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = (DjangoFilterBackend)
    filter_fields = ['name']

# class CharFilterInFilter(BaseInFilter, CharFilter):
#     pass
#
# class CountryFilter(FilterSet):
#     name = CharFilterInFilter(field_name='country__name', lookup_expr='in')
#     id = RangeFilter()
#
#     class Meta:
#         model = Country
#         fields = ['id', 'name']



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
