from flask import Flask ,jsonify
from sqlalchemy.ext.declarative import declarative_base               
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 

from .. import dbt

Base = declarative_base()

class Advertiser(Base,dbt.Model):
    __tablename__='t_advertiser'

    id_advertiser= dbt.Column ( dbt.Integer  , primary_key=True , autoincrement=True)
    company_name = dbt.Column(dbt.String(245))
    contact = dbt.Column(dbt.String(100))
    start_hour = dbt.Column(dbt.String(45))
    end_hour = dbt.Column(dbt.Time)
    email = dbt.Column(dbt.String(45))
    message = dbt.Column(dbt.String(250))


    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
      #end-def
#end-class
class Location (Base, dbt.Model): 
     __tablename__= "t_location"
     id_location = dbt.Column ( dbt.Integer , primary_key=True , unique=True , nullable =False , autoincrement=True)
     county=dbt.Column(dbt.String(45))
     island=dbt.Column(dbt.String(45))
     country=dbt.Column(dbt.String(45))
     t_advertiser_id_advertiser = dbt.Column (dbt.Integer , dbt.ForeignKey("t_advertiser.id_advertiser") ,name="t_advertiser_id_advertiser" )
   

     def to_dict(self):
         return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
   
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
     
   
    #@validates('model','passenger_number','extra_fees','price','brand','fuel_type','door_number','available')
    
    @validates('model')
    def validate_model(self,key,value):
         if value == "" : raise Exception ( "Model Incorrect")  
         else:return value
         
    @validates('passenger_number')          
    def validate_Passenger(self,key,value):
         if value == "" : raise Exception ( "Passenger Number Incorrect or null")  
         else: return value

    @validates('price')          
    def validate_price(self,key,value):
         if value == "" : raise Exception ( "price Incorrect or null")  
         else:return value

    @validates('brand')          
    def validate_brand(self,key,value):
         if value == "" : raise Exception ( "brand Incorrect or null")  
         else: return value
   
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}