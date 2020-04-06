import sys 
from flask import *
import json
sys.path.append('./')
from DB_ADMIN import db
from bson.json_util import dumps

databaseObj1 = db.database()
databaseClient1 = databaseObj1.getClient2()
clientdetail_db = databaseClient1.empdb
clintdb_collection =clientdetail_db.empdetail





def hello():
    
    return jsonify({"message": "welcome to employee section"})

def view():
    data = dumps(clintdb_collection.find({},{"_id": 0}))
    if (clintdb_collection.find({},{"_id": 0}).count()!= 0):
        return jsonify({"employe": data ,"id": userid})
    print(clintdb_collection.find({},{"_id": 0}).count())




def add_employee(data):
    employee = json.loads(data)
    name = employee["name"]
    mail = employee["mail"]
    address = employee["address"]
    mydict = {"name": name, "mail": mail, "address": address }
    clintdb_collection.insert_one(mydict)
    return {'status': "sucess"}




def update_employee(primary_key,data):
    employee = json.loads(data)
    name = employee["name"]
    address = employee["address"]
    olddata=  {'mail': primary_key}
    newdata = { "$set": { "name": name,"mail": primary_key, "address": address} }
    clintdb_collection.update_one(olddata, newdata)
    return jsonify({"emplyoee" : "emplyoee updated"})


def delete_employee(primary_key):
    clintdb_collection.delete_one({"mail": primary_key})
    return jsonify({"emplyoee": "employee deleted"})


