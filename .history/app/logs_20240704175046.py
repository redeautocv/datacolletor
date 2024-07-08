from flask import Flask ,request
from .. import main  

@main.app.route("/anuncio")
def create_anuncio():    
     return  "ddd"
