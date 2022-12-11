from django.urls import path

from .handlers.sensor import sensor, sensorById

urlpatterns = [
    path('sensor', sensor, name='allsensors'),
    path('sensor/<str:id>', sensorById, name='sensorbyid'),
]