from flask import Flask ,request
from __init__ import  create_app 
import os 

app=  create_app(os.getenv("CONFIG_MODE")) 


#DEVELOPMENT_DATABASE_URL="postgresql://psqladminun@pgsql-server-racv:H@camelo!@pgsql-server-racv.postgres.database.azure.com/racvdb"

@app.route('/ff')
def hello():
    return "Hello World!"
 
from app.logs import * 


if __name__=='__main__':
 
    print("kfkfk")
    app.run(debug=True)