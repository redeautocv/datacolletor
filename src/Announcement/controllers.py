from flask import request,jsonify
from annou.models import Announcement
from __init__ import  dbt 
import uuid

def  list_all_tables ():
  dataform = Announcement.query.all()
  form = []
  for x in dataform :
     form.append(x.toDict())
  return jsonify(form)

def create_table ():
   request_form = request.form.to_dict()
   id = str(uuid.uuid4())
   new_table = Announcement(id,
                          request_form['tipocarro'] ,
                          request_form['numerolugares'] , 
                          request_form['taxasextras'],
                          request_form['preco']  ,
                          request_form['tipocombustivel']   
                         )

   dbt.session.add(new_table)
   dbt.commit()
   response = Announcement.query.get(id).toDict()
   return jsonify(new_table)

def delete_table(account_i):
   Announcement.query.filter().delete_table()
   
 