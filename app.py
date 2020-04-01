import sys 
sys.path.append('./')
from flask import *
from AUTH import register,login
from OPERATION import crud
#import os
#from AUTH import login
app = Flask(__name__)



app.add_url_rule('/register', view_func=register.register, methods=['POST'])
app.add_url_rule('/login',view_func=login.is_exist, methods=['POST'])
app.add_url_rule('/read',view_func=crud.view, methods=['GET'])
app.add_url_rule('/create',view_func=crud.add_employee, methods=['POST'])
app.add_url_rule('/update',view_func=crud.update_employee, methods=['PUT'])
app.add_url_rule('/delete',view_func=crud.delete_employee, methods=['DELETE'])
if __name__== "__main__":
    app.run(debug = True,host='0.0.0.0')


