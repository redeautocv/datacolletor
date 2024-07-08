from flask import Flask,Blueprint , render_template
import app.models


def create_app() :
   app= Flask(__name__ )
   app.config['SCRET_KEY']='key_Secret'

   from  app.views import views
   from  app.models import models 

   app.register_blueprint(views,url_prefix='/')
   app.register_blueprint(models,url_prefix='/')
   
   return app