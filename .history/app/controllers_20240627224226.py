import requests
from bs4 import BeautifulSoup

URL = "https://caetano.cv/rent-a-car/"  
 

response = requests.get(URL)
conteudo = response.text
 

soup = BeautifulSoup(conteudo, 'html5lib')

tagNome=soup.find_all('div' ,{'id':"lp-pom-text-939"})
for x in tagNome:
    
