import sys 
from flask import *
import json
sys.path.append('./')
from DB_ADMIN import db
from bson.json_util import dumps
from AUTH import login

databaseObj = db.database()

databaseClient = databaseObj.getClient2()
clientdetail_db = databaseClient.empdb
clintdb_collection =clientdetail_db.empdetail





def view():
    employee = request.get_json()
    if (login.is_exist(employee) and employee["role"]=="manager"):

        data = dumps(clintdb_collection.find({},{"_id": 0}))
        if (clintdb_collection.find({},{"_id": 0}).count()!= 0):
            return jsonify({"employe": data})
        print(clintdb_collection.find({},{"_id": 0}).count())
    return {'status': "user not found or you are not authorized"}



def add_employee():
    employee = request.get_json()
    if (login.is_exist(employee) and (employee["role"]=="developer" or employee["role"]=="hr")):
    
        name = employee["name"]
        mail = employee["mail"]
        mydict = {"name": name, "mail": mail }
        clintdb_collection.insert_one(mydict)
        #return jsonify({'message':'user added'})
        return {'status': "sucess"}
    return {'status': "user not found or you are not authorized"}



def update_employee():
    employee = request.get_json()
    if (login.is_exist(employee) and employee["role"]=="developer"):
        
        name = employee["name"]
        mail = employee["mail"]
        olddata=  {'mail': mail}
        newdata = { "$set": { "name": name,"mail": mail } }
        clintdb_collection.update_one(olddata, newdata)
        return jsonify({"emplyoee" : "emplyoee updated"})
    return {'status': "user not found or you are not authorized"}


def delete_employee():
    employee = request.get_json()
    if (login.is_exist(employee) and employee["role"]=="hr"):
    
        data = employee['mail']
        clintdb_collection.delete_one({"mail":data})
        return jsonify({"emplyoee": "employee deleted"})
    return {'status': "user not found or you are not authorized"}

