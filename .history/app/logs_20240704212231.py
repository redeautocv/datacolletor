from flask import Flask ,request
from   main   import *
from  .controllers import list_all_tables , create_table , delete_table

@app.route("/announcement ", methods=['GET','PUT'])
def create_anuncio():    
   if request.method=='GET':
        return list_all_tables()
       
   if request.method=='PUT':
        return create_table()
   
@app.route("/alterannouncement/<account_id>")
def alter():
    if request.method=='DELETE':
        return delete_table