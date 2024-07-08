import os 
from  flask import Flask
import app
import app.initi

app=  app.initi.create_app(os.getenv("CONFIG_MODE")) 

if __name__=='__main__':
    app.run(debug=True)