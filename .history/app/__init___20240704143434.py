from flask import Flask,Blueprint , render_template

import flask_sqlalchemy 
from flask_migrate import Migrate

from .config import config

dbt = flask_sqlalchemySQLAlchemy()
migrate = Migrate()

def create_app(config_mode) :
   app= Flask(__name__ )
   app.config['SCRET_KEY']='key_Secret'
   app.config.from_object(config[config_mode])

   from  .views import views
   from  .models import models 

   app.register_blueprint(views,url_prefix='/')
   app.register_blueprint(models,url_prefix='/')
   
   dbt.init_app(app)
   migrate.init_app(app, dbt)
   return app