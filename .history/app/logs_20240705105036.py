from flask import Flask ,request
from   main   import app
from  app.controllers import create_table , delete_table

@app.route("/announcement ", methods=['GET','PUT'])
def create_anuncio():    
   if request.method=='GET':
        retuen "rn list_all_tables()"
       
   if request.method=='PUT':
        return create_table()
   
@app.route("/alterannouncement/<account_id>")
def alter(account_id):
    if request.method=='DELETE':
        return delete_table(account_id)