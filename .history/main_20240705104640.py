from flask import Flask ,request
from  app  import create_app
import os 
from 
app=  create_app(os.getenv("CONFIG_MODE")) 


 
@app.route('/ff')
def hello():
    return "Hello World!"


from  app import logs 

@logs.app.route("/announcement ", methods=['GET','PUT'])
def create_anuncio():    
   if request.method=='GET':
        return list_all_tables()
       
   if request.method=='PUT':
        return create_table()
   

if __name__=='__main__':
 
    print("kfkfk")
    app.run(debug=True)