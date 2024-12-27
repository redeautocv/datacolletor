from  . import  create_app 
import os 
  


 
config_mode = os.getenv('CONFIG_MODE') or 'development'
app = create_app(config_mode)

#DEVELOPMENT_DATABASE_URL="postgresql://psqladminun@pgsql-server-racv:H@camelo!@pgsql-server-racv.postgres.database.azure.com/racvdb"
#psql -h pgsql-server-racv.postgres.database.azure.com -U psqladminun@pgsql-server-racv -d racvdb
@app.route('/')
def hello():
    
    return "Hello World!"

from  .caetano_renta_car.logs import *
 
if __name__=='__main__':
 
     app.run(debug=True)