# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import JSONB
from ... import dbt


class DataCollector(dbt.Model):
    __tablename__ = 't_datacollector'

    id = dbt.Column(dbt.Integer, primary_key=True)
    data_coleta = dbt.Column(dbt.String(255))
    nome_empresa = dbt.Column(dbt.String(255), nullable=False)
    dados_anuncios = dbt.Column(JSONB, nullable=False)
    dados_localizacao = dbt.Column(JSONB, nullable=False)

    def __repr__(self):
        return f'<DataCollector {self.nome_empresa}>'