from flask import Flask
from sqlalchemy.inspection import inspect
from sqlalchemy import Column , String , Integer , ForeignKey
from sqlalchemy.orm import relationship
from .. import dbt

class Announcement(dbt.Model):
    __tablename__='t_ad'
    id_ad = dbt.Column(dbt.Integer, primary_key=True, nullable=False, unique=True , autoincrement=True)
    model = dbt.Column(dbt.String(45))
    passenger_number = dbt.Column(dbt.String(45))
    extra_fees= dbt.Column(dbt.String(45))
    price= dbt.Column(dbt.String(45))
    brand= dbt.Column(dbt.String(45))
    fuel_type=dbt.Column(dbt.String(45))
    door_number=dbt.Column(dbt.String(45))
    available= dbt.Column(dbt.Boolean)
    t_advertiser_id_advertiser= dbt.Column(dbt.Integer, dbt.ForeignKey("t_advertiser.id_advertiser") )
    
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Advertiser(dbt.Model):

    __tablename__='t_advertiser'
    id_advertiser= dbt.Column ( dbt.Integer ,unique=True ,nullable =False, primary_key=True , autoincrement=True)
    company_name = dbt.Column ( dbt.String(45) )
    contact = dbt.Column ( dbt.String(45))
    start_hour= dbt.Column (dbt.String(45))
    end_hour= dbt.Column(dbt.Time)
    email = dbt.Column (dbt.String(45))
    message= dbt.Column(dbt.String(45))
    locations = dbt.relationship('Location' , backref='Advertiser' )
    ads = dbt.relationship('Announcement', backref='Advertiser' )  

    
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        

class Location ( dbt.Model):
     __tablename__= "t_location"
     id_location = dbt.Column ( dbt.Integer , primary_key=True , unique=True , nullable =False , autoincrement=True)
     county=dbt.Column(dbt.String(45))
     island=dbt.Column(dbt.String(45))
     country=dbt.Column(dbt.String(45))
     t_advertiser_id_advertiser = dbt.Column (dbt.Integer , dbt.ForeignKey("t_advertiser.id_advertiser") ,name="t_advertiser_id_advertiser" )
   

     def to_dict(self):
         return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
 