import requests
from bs4 import BeautifulSoup

URL = "https://caetano.cv/rent-a-car/"  
 

response = requests.get(URL)
conteudo = response.text
 

soup = BeautifulSoup(conteudo, 'html5lib')

tagNome=soup.find_all('DIV' ,{'id':"lp-pom-text-939"})
if tagNome:
    x = tagNome.find_all ( '')
