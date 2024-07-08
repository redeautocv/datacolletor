from flask import Flask ,request
from ..main import app

@app.route("/anuncio", methods=['GET', 'POST'])
def creta_anuncio():
    if request.method =='GET':  
         return  pass
