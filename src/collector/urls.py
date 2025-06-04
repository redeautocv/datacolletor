import requests 
from flask import  request, jsonify  

from  .controllers import collect
from  ..app import app

@app.route("/start")
def data_collect():
     collect()
     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP


 
#end-def

