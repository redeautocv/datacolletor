from flask import Flask ,jsonify
from sqlalchemy.ext.declarative import declarative_base               
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 

from ... import dbt

Base = declarative_base()

class Listing( dbt.Model): #anuncio
    __tablename__='t_ad'
    
    id_ad = dbt.Column(dbt.Integer, primary_key=True, nullable=False, unique=True , autoincrement=True)
    model = dbt.Column(dbt.String(45))
    passenger_number = dbt.Column(dbt.String(45))
    extra_fees= dbt.Column(dbt.String(45))
    price= dbt.Column(dbt.String(45))
    brand= dbt.Column(dbt.String(45))
    fuel_type=dbt.Column(dbt.String(45))
    door_number=dbt.Column(dbt.String(45))
    available= dbt.Column(dbt.String(45))
    t_advertiser_id_advertiser= dbt.Column(dbt.Integer, dbt.ForeignKey("t_advertiser.id_advertiser") )