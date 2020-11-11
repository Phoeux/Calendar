from django.urls import path

from app_auth.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
]
