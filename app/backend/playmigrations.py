import sqlite3
import os
import datetime

database = sqlite3.connect("db.sqlite3")
curs = database.cursor()
try:
    ids = [data[0] for data in curs.execute("SELECT id from Migrations;").fetchall()]
except Exception as e:
    curs.execute("CREATE TABLE Migrations(id varchar(30) PRIMARY KEY, version varchar(15), integration_date timestamp);")
    ids = []
#load migrations
print(f"migration{'s' if len(ids)>1 else ''} already integrated : {','.join(ids) if len(ids) else 'none'}")

migrations = []
for file in os.listdir("./migrations"):
    path = "./migrations/"+file
    id=file.split(".")[0]
    if os.path.isfile(path) and file.endswith("sql") and id not in ids:
        with open(path, "r") as mig:
            migcontent = ""
            for line in mig.readlines():
                version = "0.0.1"
                if line.startswith("--m\\"):
                    mc = line.split("--m\\")[1]
                    if mc.startswith("productversion"):
                        version = mc.split(":")[1]
                else:
                    migcontent += line
            migrations.append({
                "id":id,
                "content":migcontent,
                "version":version
            })
print(f"accumulated {len(migrations)} migrations")
mig_count = 0
migrations.sort(key=lambda o: o["version"])
for mig in migrations:    
    print(f"executing migration '{mig['id']}' [{'='*round(mig_count/len(migrations)*100.)}{' '*round((len(migrations)-mig_count)/len(migrations)*100.)}]", end="\r")
    try:
        curs.executescript(mig["content"])
        migration_add_poll = f"INSERT INTO Migrations(id, version, integration_date) VALUES('{mig['id']}', '{mig['version']}', '{datetime.datetime.now()}')"
        curs.execute(migration_add_poll)
        database.commit()
    except Exception as e:
        print(f"ERROR : An exception occured while execution of '{mig['id']}', aborting migrations. \n    Detail: {e}")
        break
    mig_count += 1
    print(f"executing migration '{mig['id']}' [{'='*round(mig_count/len(migrations)*100.)}{' '*round((len(migrations)-mig_count)/len(migrations)*100.)}]", end="\r")
print("\n")
print(f"compiled {mig_count} migrations")