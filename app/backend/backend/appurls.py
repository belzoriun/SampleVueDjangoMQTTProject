from django.urls import path

from .handlers.sensor import sensor, sensorById
from .handlers.user import user, userById

urlpatterns = [
    path('sensor', sensor, name='allsensors'),
    path('sensor/<str:id>', sensorById, name='sensorbyid'),
    path('user', user, name='users'),
    path('user/<str:id>', userById, name='userbyid'),
]