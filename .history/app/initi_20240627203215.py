from flask import Flask,Blueprint , render_template

x = 0;

def create_app() :
   app= Flask(__name__ )
   app.config['SCRET_KEY']='key_Secret'

   from app.views import views
   from

   app.register_blueprint(views,url_prefix='/')
   return app