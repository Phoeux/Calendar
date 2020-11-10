from django.urls import path

from app_calendar import views

urlpatterns = [
    path('list/', views.ListHolidays.as_view(), name='list'),
    path('list/<str:country>/', views.ListHolidays.as_view(), name='list_with_year'),
]