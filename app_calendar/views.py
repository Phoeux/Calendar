import holidays
from django.http import request
from django.shortcuts import render
from ics import Calendar, Event
from rest_framework.generics import ListAPIView

from app_calendar.models import Holiday
from app_calendar.serializer import HolidaySerializer, CountrySerializer, EventSerializer, UserSerializer


class ListHolidays(ListAPIView):
    serializer_class = HolidaySerializer

    # def get_queryset(self):
    #     if self.kwargs.get('year'):
    #         return Holiday.objects.filter(date=self.kwargs.get('year'))
    #     return Holiday.objects.all()

    # def fill_colendar_for_country(self, country):
    #     url = f'https://www.officeholidays.com/ics/ics_country.php?tbl_country={country}'
    #     res = request.get(url).text
    #     c = Calendar(res)





    # def fill_colendar_for_country(self, country):
    #     # url = f'https://www.officeholidays.com/ics/ics_country.php?tbl_country={country}'
    #     try:
    #         calendar = Calendar(request.get(url).text)
    #     except:
    #         return None
    #     for event in calendar.events:
    #         h = Holiday(
    #             title=event.name,
    #             date_start=event.begin.date(),
    #             duration=event.duration,
    #             description=event.description,
    #             county=country
    #         )
    #     try:
    #         h.save()
    #     except:
    #         pass