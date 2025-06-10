import requests 
from flask import jsonify  

from  .controllers import collect,create
from  ..app import app

@app.route("/start")
def data_collect():
     data_json = collect() 
     create(data_json)
     resposta = requests.post("http://localhost:5001/received-data", json=data_json)

     return jsonify({"status": "coleta iniciada com sucesso"})  # resposta HTTP
     
 
#end-def

