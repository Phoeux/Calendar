from django.urls import path

from app_calendar import views

urlpatterns = [
    path('holidays/', views.ListHolidays.as_view(), name='holidays_full_list'),
    path('holidays/<int:id>/', views.ListCountryHolidays.as_view(), name='holidays_country_list'),

    path('holidays/<int:id>/<int:year>/', views.ListHolidays.as_view(), name='year_holidays'),
    path('holidays/<int:id>/<int:year>/<int:month>/', views.ListHolidays.as_view(), name='month_holidays'),
    path('holidays/create/', views.CreateHolidays.as_view(), name='create_holidays'),

    path('countries/', views.ListCountries.as_view(), name='countries_list'),
    path('countries/<str:name>/', views.ListCountries.as_view(), name='countries_list'),
]