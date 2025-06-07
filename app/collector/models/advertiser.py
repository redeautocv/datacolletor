from flask import Flask ,jsonify
from sqlalchemy.ext.declarative import declarative_base               
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 

from ... import dbt

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