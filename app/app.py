import os 

from  . import  create_app 
  
config_mode = os.getenv('CONFIG_MODE') or 'development'
app = create_app(config_mode)

@app.route('/')
def hello():
    return "Hello World!"

#from  .collector.urls import *
from  app.collector.routes.anuncio_route import *
from  app.collector.routes.utilizador_route import *

if __name__=='__main__':
 
     app.run(debug=True)