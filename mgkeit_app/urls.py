from django.urls import path
from .views import *
from .models import *


urlpatterns = [
    path('user/', PersonView.as_view()),
    path('user/<int:pk>', PersonView.as_view()),
    path('timetable/', TimetableView.as_view()),
    path('timetable/<str:pk>', TimetableView.as_view()),
]
