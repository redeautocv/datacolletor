import requests ,jsonify
from bs4 import BeautifulSoup
from .models import publicar


def  list_all_tables ():
  dataform = publicar.query.all()
  form = []
  for x in dataform :
     form.append(x)
  return jsonify(form)

def create_table ():
   response = requests.form.to_dict()
   
   new_table = publicar ( tipoCarro , numeroLugares  , taxasExtras , preco  , tipoCombustivel   )

