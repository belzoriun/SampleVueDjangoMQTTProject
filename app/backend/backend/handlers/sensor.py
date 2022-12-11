from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import sqlite3
import json
import uuid

def getSensor(curs, id):
    sensor = curs.execute("SELECT name FROM Sensor WHERE id=?", [id]).fetchone()
    if sensor:
        return HttpResponse(json.dumps({
            "code":"OK", 
            "name":sensor[0]
        }))
    else:
        return HttpResponseBadRequest(json.dumps({
            "code":"SENSOR_NOT_FOUND"
        }))

def sensor(request):
    database = sqlite3.connect("db.sqlite3")
    curs = database.cursor()
    result = None
    if request.method == "GET":
        if "sensor" in request.GET:
            result = getSensor(curs, request.GET.get("sensor"))
        else:
            sensors = curs.execute("SELECT id, name FROM Sensor").fetchall()
            result = HttpResponse(json.dumps({
                "code":"OK", 
                "sensors":[{"id":id, "name":name} for id, name in sensors]
            }))
    elif request.method == "POST":
        name = request.POST.get("name")
        if not name:
            result = HttpResponseBadRequest(json.dumps({
                "code":"NO_NAME"
            }))
        id = uuid.uuid4()
        print(str(id))
        curs.execute("INSERT INTO Sensor(id, name) VALUES(?, ?);", [str(id), name])
        database.commit()
        result = HttpResponse(json.dumps({
            "code":"OK"
        }))
    else:
        result = HttpResponseNotAllowed(["GET", "POST"])
    curs.close()
    database.close()
    return result

def sensorById(request, id):
    database = sqlite3.connect("db.sqlite3")
    curs = database.cursor()
    result = None
    if request.method == "DELETE":
        curs.execute("DELETE FROM Sensor WHERE id=?", [id])
        database.commit()
        result = HttpResponse(json.dumps({
            "code":"OK"
        }))
    elif request.method == "GET":
        result = getSensor(curs, id)
    else:
        result = HttpResponseNotAllowed(["GET", "DELETE"])
    curs.close()
    database.close()
    return result