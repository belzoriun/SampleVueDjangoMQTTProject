from . import database
import uuid

def add_user(firstname, lastname, email, login):
    id = uuid.uuid4()
    database.Database()\
        .execute("INSERT INTO User(id, firstname, lastname, email) VALUES(?, ?, ?, ?);", 
            [str(id), firstname, lastname, email])\
        .execute("INSERT INTO UserLogin(user_id, login) VALUES (?, ?);", [str(id), login])\
        .commit()
    return id

def get_user_info(id):
    data = database.Database()\
        .execute("SELECT firstname, lastname, email, login FROM User JOIN UserLogin ON User.id = UserLogin.user_id WHERE id=?;", [str(id)])\
        .fetchone()
    if not data: return None
    return {
        "firstname":data[0],
        "lastname":data[1],
        "email":data[2],
        "login":data[3]
    }

def set_user_info(id, firstname, lastname, email, login):
    database.Database()\
        .execute("UPDATE User SET firstname=?, lastname=?, email=? WHERE id=?;", 
            [firstname, lastname, email, str(id)])\
        .execute("UPDATE UserLogin SET login=? WHERE user_id=?;", [login,str(id)])\
        .commit()