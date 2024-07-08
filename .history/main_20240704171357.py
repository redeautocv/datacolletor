from flask import Flask
from  app  import create_app
import os 
app=  create_app(os.getenv("CONFIG_MODE")) 
@app.route('/ff')
def hello():
    return "Hello World!"

import .app import logs

if __name__=='__main__':
    print("kfkfk")
    app.run(debug=True)