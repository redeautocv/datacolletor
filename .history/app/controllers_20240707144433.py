from flask import request,jsonify
from bs4 import BeautifulSoup
from .models import publicar
from .  import dbt
import uuid

def  list_all_tables ():
  dataform = publicar.query.all()
  form = []
  for x in dataform :
     form.append(x.toDict())
  return jsonify(form)

def create_table ():
   request_form = request.form.to_dict()
   id = str(uuid.uuid4())
   new_table = publicar ( id =id,
                          tipocarro=request_form['tipocarro'] ,
                          numerolugares=request_form['numerolugares'] , 
                          taxasextras= request_form['taxasextras'],
                          preco=request_form['preco']  ,
                          tipocombustivel=request_form['tipocombustivel']   
                         )

   dbt.session.add(new_table)
   dbt.commit()
   response = publicar.query.get(id).toDict()
   return jsonify(new_table.toDict())

def delete_table(account_i):
   publicar.query.delete_table()
   dbt.session.commit () 
 