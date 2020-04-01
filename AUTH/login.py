import sys 
from flask import *
sys.path.append('./')
from DB_ADMIN import db



databaseObj = db.database()

databaseClient = databaseObj.getClient1()
db = databaseClient.login 
collection =db.logindetail

def is_exist(employee):
    for id in collection.find({},{"_id": 0}):
        print("crunt id ="+ id['userid'])
        if((employee["userid"]==id['userid'] and employee["password"]==id["password"]) or employee["role"]==id["role"]):
            print("match")
            return True
    return False




