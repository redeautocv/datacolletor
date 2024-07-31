from flask import  request
from  .controllers import list_all_tables_Announcemet,list_all_tables_advertiser,create_tables ,delete_account_controller
from  ..main import app

@app.route("/Annout")
def read_announcement():    
   if request.method=='GET':
        return list_all_tables_Announcemet()
        
@app.route("/advert")
def read_advertiser():
    if request.method =='GET':
        return list_all_tables_advertiser()

@app.route("/create")
def create_database():
    if request.method=="GET":
       return create_tables()



@app.route("/alterannouncement/<account_id>")
def alter(account_id):
    if request.method=='DELETE':
        return delete_account_controller(account_id)
