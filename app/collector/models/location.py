from flask import Flask ,jsonify
from sqlalchemy.ext.declarative import declarative_base               
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 

from ... import dbt

Base = declarative_base()

class Location (Base, dbt.Model): 
     __tablename__= "t_location"
     id_location = dbt.Column ( dbt.Integer , primary_key=True , unique=True , nullable =False , autoincrement=True)
     county=dbt.Column(dbt.String(45))
     island=dbt.Column(dbt.String(45))
     country=dbt.Column(dbt.String(45))
     t_advertiser_id_advertiser = dbt.Column (dbt.Integer , dbt.ForeignKey("t_advertiser.id_advertiser") ,name="t_advertiser_id_advertiser" )
   

     def to_dict(self):
         return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
   