from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

dbt = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode) :
   app= Flask(__name__ )
   app.config['SCRET_KEY']='key_Secret'
   app.config.from_object(config[config_mode])

 
   
   dbt.init_app(app)
   migrate.init_app(app, dbt)
   return app