import requests
from bs4 import BeautifulSoup

URL = "https://caetano.cv/rent-a-car/"  
 

response = requests.get(URL)
conteudo = response.text
 
marcaCarro=[]
numeroLugares=[]
taxasextras=[]
preco=[]

soup = BeautifulSoup(conteudo, 'html5lib')

tagNome=soup.find_all('div' ,{'id':"lp-pom-text-939"})
for x in tagNome:
      marcaCarro=x.find_all('strong')
         
         
taglugares=soup.find_all('div' ,{'id':"lp-pom-text-940"})
for x in taglugares:
      numeroLugares=x.find_all('strong')


tagextras=soup.find_all('div' ,{'id':"lp-pom-text-941"})
for x in tagextras:
      taxasextras=x.find_all('strong')


tagpreco=soup.find_all('div' ,{'id':"lp-pom-text-942"})
for x in tagpreco:
      preco=x.find_all('strong')
