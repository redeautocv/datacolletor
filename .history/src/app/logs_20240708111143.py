from flask import Flask ,request
from   src.app.controllers   import list_all_tables ,
 
@app.route("/announcement", methods=['GET','POST'])
def create_anuncio():    
  
   if request.method=='GET':
        return list_all_tables()
        
   if request.method=='POST':
        return create_table()
   
@app.route("/alterannouncement/<account_id>")
def alter(account_id):
    if request.method=='DELETE':
        return delete_table(account_id)