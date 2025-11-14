from sqlalchemy.inspection import inspect
from sqlalchemy.orm import validates 


from app import dbt

class Anunciante(dbt.Model):
    __tablename__='t_anunciante'

    id_anunciante = dbt.Column ( dbt.Integer  , primary_key=True , autoincrement=True)
    nome = dbt.Column(dbt.String(500))
    sexo = dbt.Column(dbt.String(10))
    telefone = dbt.Column(dbt.String(2000))
    link = dbt.Column(dbt.String(300))
    email = dbt.Column(dbt.String(300))
    foto = dbt.Column(dbt.String(300))
    ilha = dbt.Column(dbt.String(300))
    descricao = dbt.Column(dbt.String(1000))
    concelho = dbt.Column(dbt.String(300))
    horario_funcionamento = dbt.Column(dbt.String(2000))
    tipo = dbt.Column(dbt.String(1000))
    endereco = dbt.Column(dbt.String(2000))
    audit_user = dbt.Column(dbt.String(300))
    audit_timestamp = dbt.Column(dbt.String(550))


    def to_dict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
 
    
    def to_dict_id(self):
        return { "id_anunciante":self.id_anunciante}
 
      #end-def
#end-class