from flask import Flask,  Blueprint 
import psycopg2
from __init__ import  dbt 
from sqlalchemy.inspection import inspect

class  publicar(dbt.Model):

    id = dbt.Column(dbt.String(50), primary_key=True, nullable=False, unique=True)
    tipocarro  = dbt.Column(dbt.String(50))
    numerolugares  = dbt.Column(dbt.String(50))
    taxasextras = dbt.Column(dbt.String(50))
    preco=dbt.Column(dbt.String(50))
    
    def __init__(self,tipocarro,numerolugares,taxasextras,preco) :
        id=self.id
        tipocarro=self.tipocarro
        numerolugares=self.numerolugares
        taxasextras=self.taxasextras
        preco=self.preco

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


