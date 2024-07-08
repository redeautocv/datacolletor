from flask import Flask ,request
from  src. import create_app
import os 
from src.app.controllers import list_all_tables, create_table ,delete_table
app=  create_app(os.getenv("CONFIG_MODE")) 


 
@app.route('/ff')
def hello():
    return "Hello World!"
 
 
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

 
 
if __name__=='__main__':
 
    print("kfkfk")
    app.run(debug=True)