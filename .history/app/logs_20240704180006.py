from flask import Flask ,request
from   main   import *

@app.route("/anuncio ", methods=['GET','PUT'])
def create_anuncio():    
   IF request.method