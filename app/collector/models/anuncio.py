from flask import Flask ,jsonify
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 

from app import dbt

class Anuncio(dbt.Model): #anuncio
    __tablename__='t_anuncio'
    
    id_anuncio = dbt.Column(dbt.Integer, primary_key=True, nullable=False, unique=True , autoincrement=True)
    modelo  = dbt.Column(dbt.String(45))
    marca = dbt.Column(dbt.String(45))
    numero_passageiro = dbt.Column(dbt.String(900))
    combustivel = dbt.Column(dbt.String(900))
    preco = dbt.Column(dbt.String(45))
    ano = dbt.Column(dbt.String(45))
    condicoes = dbt.Column(dbt.String(150))
    caucao = dbt.Column(dbt.String(45))
    fotografia = dbt.Column(dbt.String(45))
    transmissao = dbt.Column(dbt.String(900))
    link = dbt.Column(dbt.String(500))
    ar_condicionado = dbt.Column(dbt.String(45))
    data = dbt.Column(dbt.String(45))
    gps = dbt.Column(dbt.String(45))
    disponibilidade = dbt.Column(dbt.String(45))
    audit_user = dbt.Column(dbt.String(45))
    audit_timestamp = dbt.Column(dbt.String(45))
    id_anunciante = dbt.Column(dbt.Integer, dbt.ForeignKey("t_anunciante.id_anunciante") )
     
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