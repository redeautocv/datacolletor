from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

dbt = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode) :
   app= Flask(__name__ )
   app.config['SCRET_KEY']='key_Secret'
   app.config.from_object(config[config_mode])

   # from  .models import models 

   # app.register_blueprint(models,url_prefix='/')
   
   dbt.init_app(app)
   migrate.init_app(app, dbt)
   return app