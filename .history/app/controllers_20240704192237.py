import requests ,jsonify
from bs4 import BeautifulSoup
from .models import publicar

def  list_all_tables ():
  dataform = publicar.query.all()
  
  for x in dataform :
