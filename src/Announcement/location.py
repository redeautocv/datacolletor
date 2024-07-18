from __init__ import dbt
from sqlalchemy.inspection import inspect


class Location ( dbt.Model):
     
     id_location = dbt.Column ( dbt.integer , primary_key=True , unique=True , nullable =True)
     county=dbt.Column(dbt.String(45))
     island=dbt.Column(dbt.String(45))
     country=dbt.Column(dbt.String(45))
     id_advertiser= dbt.column (dbt.Integeter , dbt.forgeinkey("t_advertiser.id") )
     advertisers= dbt.relationship('advertiser', back_populates='Location')

     def __init__(self  , id_location ,county , island , country ,id_advertiser):
          self.id_location=  id_location
          self.county=county
          self.island=island
          self.country=country 
          self.id_advertiser=id_advertiser

     def to_dict(self):
         return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
 