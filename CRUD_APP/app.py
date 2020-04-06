import sys 
sys.path.append('./')
from flask import *
from OPRATION import crud
import os

app = Flask(__name__)




app.add_url_rule('/read',view_func=crud.view, methods=['GET','POST'])
app.add_url_rule('/create/<data>',view_func=crud.add_employee, methods=['POST'])
app.add_url_rule('/update/<primary_key>/<data>',view_func=crud.update_employee, methods=['PUT','POST'])
app.add_url_rule('/delete/<primary_key>',view_func=crud.delete_employee, methods=['POST','DELETE'])




    

if __name__== "__main__":
    port = int(os.environ.get('PORT', 5004))
    app.run(host='0.0.0.0', port=port)
