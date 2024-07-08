from flask import Flask ,request
from   main   import *
from  
@app.route("/announcement ", methods=['GET','PUT'])
def create_anuncio():    
   if request.method=='GET':
        return 'X'
       
   if request.method=='PUT':
        return 'X'
   
@app.route("/alterannouncement/<account_id>")
def alter():
    if request.method=='DELETE':
        return 'x'