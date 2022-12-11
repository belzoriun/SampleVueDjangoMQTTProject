from . import database
import uuid

def get_sensor(id):
    print(id)    
    sensor = database.Database()\
        .execute(lambda query: query.appendQuery("SELECT name FROM Sensor WHERE id=?", [id]))\
        .fetchone()
    return sensor[0] if sensor else None

def get_all_sensors():
    return [{"id":id, "name":name} for id, name in database.Database()\
        .execute(lambda query:query.appendQuery("SELECT id, name FROM Sensor")).fetchall()]

def add_sensor(name):       
        id = uuid.uuid4()
        database.Database()\
            .execute(lambda query:query.appendQuery("INSERT INTO Sensor(id, name) VALUES(?, ?);", [str(id), name]))\
            .commit()
        return str(id)

def delete_sensor(id):
    database.Database()\
        .execute(lambda query:query.appendQuery("DELETE FROM Sensor WHERE id=?", [id]))\
        .commit()