from __init__ import dbt
from sqlalchemy.inspection import inspect

class Advertiser(dbt.Model):


    __tablename__='t_advertiser'
    id_advertiser= dbt.column ( dbt.Integer ,unique=True , nullable=True , primary_key=True)
    contact_name = dbt.column ( dbt.Integer , primary_key=True)
    contact = dbt.column ( dbt.Integer)
    start_time= dbt.column (dbt.Date)
    end_time= dbt.time(dbt.date)
    email = dbt.column (dbt.String(45))
    message= dbt.column(dbt.String(45))
    locations = dbt.relationship('Location' , back_populates='Advertiser')  
    
    
    def __init__(self ,name,contact,start_time,end_time , email , message ) :
          self.name= name
          self.contact=contact
          self.start_time=start_time
          self.end_time=end_time
          self.email=email
          self.message= message
          
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        



