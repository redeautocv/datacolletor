from flask import Flask ,request
from   main   import *

@app.route("/anuncio ", methods=['GET','PUT'])
def create_anuncio():    
   if request.method=='GET':
        return 'X'
       
   if request.method=='PUT':
        return 'X'
   
