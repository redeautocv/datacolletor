import os 
from  flask import Flask
import app
import app.initi
from . import create_app
app=   create_app(os.getenv("CONFIG_MODE")) 
@app.route('/')
def hello():
    return "Hello World!"

if __name__=='__main__':
    app.run(debug=True)