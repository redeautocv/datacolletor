from flask import Flask
from sqlalchemy.inspection import inspect
from __init__ import dbt

class Announcement(dbt.Model):
    __tablename__='t_ad'
    id_prover = dbt.Column(dbt.Integer, primary_key=True, nullable=False, unique=True)
    model = dbt.Column(dbt.String(45))
    passenger_number = dbt.Column(dbt.String(45))
    extra_fees= dbt.Column(dbt.String(45))
    price= dbt.Column(dbt.String(45))
    brand= dbt.Column(dbt.String(45))
    fuel_type=dbt.Column(dbt.String(45))
    door_number=dbt.Column(dbt.String(45))
    available= dbt.Column(dbt.boolean)
    id_advertiser= dbt.column(dbt.Integer, dbt.foreignkey("t_advertiser.id") , unique=True, nullable=True )
    
    def __init__(self, id_prover,model,passenger_number, extra_fees, price ,brand , fuel_type , door_number ,available ,id_advertiser  ):
        self.id_prover = id
        self.model = model
        self.passenger_number = passenger_number
        self.extra_fees = extra_fees
        self.price = price
        self.brand=brand
        self.fuel_type=fuel_type
        self.door_number=door_number
        self.available=available
        self.id_advertiser=id_advertiser

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
