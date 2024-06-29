import requests
from bs4 import BeautifulSoup

URL = "https://caetano.cv/rent-a-car/"  
 

response = requests.get(URL)
conteudo = response.text
 

soup = BeautifulSoup(conteudo, 'html5lib')

tituloNoticia=soup.find_all('str',{'class':'title'})
