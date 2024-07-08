from flask import Flask ,request
from  app  import create_app
import os 
from app.controllers import list_all_tables, create_table ,delete_table
app=  create_app(os.getenv("CONFIG_MODE")) 


 
@app.route('/ff')
def hello():
    return "Hello World!"
 
 from app import 

 
 
if __name__=='__main__':
 
    print("kfkfk")
    app.run(debug=True)