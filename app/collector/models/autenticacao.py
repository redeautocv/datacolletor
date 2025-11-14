from flask import jsonify
from flask import Flask 
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 

from app import dbt

class Autenticacao ( dbt.Model): 
     __tablename__= "t_autenticacao"
     id_utilizador= dbt.Column ( dbt.Integer  , primary_key=True , autoincrement=True)
     password = dbt.Column ( dbt.String(45))
     email = dbt.Column(dbt.String(45))
     token_social_media = dbt.Column(dbt.String(45))
     user_name = dbt.Column(dbt.String(45))
     audit_user = dbt.Column(dbt.String(150))
     audit_timestamp = dbt.Column(dbt.String(250))
     id_anuncio = dbt.Column (dbt.Integer , dbt.ForeignKey("t_anunciante.id_anunciante") )
   

     def to_dict(self):
         return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
