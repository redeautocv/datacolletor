# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import JSONB
from ... import dbt


class DataCollector(dbt.Model):
    __tablename__ = 't_datacollector'

    id = dbt.Column(dbt.Integer, primary_key=True)
    link = dbt.Column(dbt.String(255))
    anunciante = dbt.Column(dbt.String(255), nullable=False)
    dados = dbt.Column(JSONB, nullable=False)
    audit_user = dbt.Column(dbt.String(300))
    audit_timestamp = dbt.Column(dbt.DateTime)

    def __repr__(self):
        return f'<DataCollector {self.nome_empresa}>'   