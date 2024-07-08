from flask import Flask,Blueprint , render_template
import app.models import SQLAlchemy
from flask_migrate import Migrate

from .config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app() :
   app= Flask(__name__ )
   app.config['SCRET_KEY']='key_Secret'

   from  app.views import views
   from  app.models import models 

   app.register_blueprint(views,url_prefix='/')
   app.register_blueprint(models,url_prefix='/')
   
   return app