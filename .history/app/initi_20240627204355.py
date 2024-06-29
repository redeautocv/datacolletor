from flask import Flask,Blueprint , render_template



def create_app() :
   app= Flask(__name__ )
   app.config['SCRET_KEY']='key_Secret'

   from app.views import views
   from app.
   app.register_blueprint(views,url_prefix='/')
   return app