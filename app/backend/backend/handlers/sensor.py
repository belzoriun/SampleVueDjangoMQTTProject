from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json
from ..managers import sensormanager

def getSensor(id):
    sensor = sensormanager.get_sensor(id)
    if sensor:
        return HttpResponse(json.dumps({
            "code":"OK", 
            "name":sensor
        }))
    else:
        return HttpResponseBadRequest(json.dumps({
            "code":"SENSOR_NOT_FOUND"
        }))

def sensor(request):
    result = None
    if request.method == "GET":
        if "sensor" in request.GET:
            result = getSensor(request.GET.get("sensor"))
        else:
            result = HttpResponse(json.dumps({
                "code":"OK", 
                "sensors":sensormanager.get_all_sensors()
            }))
    elif request.method == "POST":
        name = request.POST.get("name")
        if not name:
            result = HttpResponseBadRequest(json.dumps({
                "code":"NO_NAME"
            }))
        id = sensormanager.add_sensor(name)
        result = HttpResponse(json.dumps({
            "code":"OK", "id":id
        }))
    else:
        result = HttpResponseNotAllowed(["GET", "POST"])
    return result

def sensorById(request, id):
    result = None
    if request.method == "DELETE":
        sensormanager.delete_sensor(id)
        result = HttpResponse(json.dumps({
            "code":"OK"
        }))
    elif request.method == "GET":
        result = getSensor(id)
    else:
        result = HttpResponseNotAllowed(["GET", "DELETE"])
    return result