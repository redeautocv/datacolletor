import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from  .config import config


dbt = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode) :
   app= Flask(__name__ )
   app.config.from_object(config[config_mode])

    
   dbt.init_app(app)
   migrate.init_app(app, dbt)
   return app