import requests ,jsonify
from bs4 import BeautifulSoup
from .models import publicar
from .  import dbt

def  list_all_tables ():
  dataform = publicar.query.all()
  form = []
  for x in dataform :
     form.append(x)
  return jsonify(form)

def create_table ():
   response = requests.form.to_dict()
   
   new_table = publicar ( tipoCarro=response["tipocarro"] ,
                          numeroLugares=response["numeroLugares"] , 
                          taxasExtras= response["taxasExtras"],
                          preco=response["preco"]  ,
                          tipoCombustivel=["tipoCombustivel"]   )

   dbt.session.add(new_table)
   dbt.commit()
   return jsonify(new_table.toDict())

def delete_table(a) 
 