from flask import request,jsonify
from bs4 import BeautifulSoup
from .models import publicar
from .  import dbt
import uuid

def  list_all_tables ():
  dataform = publicar.query.all()
  form = []
  for x in dataform :
     form.append(x)
  return jsonify(form)

def create_table ():
   response = request.form.to_dict()
   id = str(uuid.uuid4())
   new_table = publicar ( id =id,
                          tipoCarro=request_form["tipocarro"] ,
                          numeroLugares=request_form["numeroLugares"] , 
                          taxasExtras= request_form["taxasExtras"],
                          preco=request_form["preco"]  ,
                          tipoCombustivel=request_form["tipoCombustivel"]   )

   dbt.session.add(new_table)
   dbt.commit()
   return jsonify(new_table.toDict())

def delete_table(account_i):
   publicar.query.delete_table()
   dbt.session.commit () 
 