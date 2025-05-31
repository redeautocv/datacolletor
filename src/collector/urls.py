import requests 
from flask import  request, jsonify  

from  .controllers import collect
from  ..app import app

@app.route("/start")
def data_collect():
     collect()
     return jsonify({"message": "Coleta iniciada com sucesso"})


 
#end-def

