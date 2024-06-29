import requests
from bs4 import BeautifulSoup

URL = "https://caetano.cv/rent-a-car/"  
 

response = requests.get(URL)
conteudo = response.text
 
marcaCarro=[]
numeroLugares=[]
taxasextras=[]
preco=[]
intervalo=[]

soup = BeautifulSoup(conteudo, 'html5lib')
tagsSites=soup.find_all('div' ,{'class':"lp-element lp-pom-box"})

for y in tagsSites:
    intervalo.append(y['id'])
    

intervaloAnuncio (intervalo)






def intervaloAnuncio (intervalos):
    for i in len(intervalos):
              intervalos[1].spli
     

"""
id= tagNome['id']


for x in tagNome:
      marcaCarro=x.find_all('strong')
         
         
taglugares=soup.find_all('div' ,{'id':"lp-pom-text-940"})
for x in taglugares:
      numeroLugares=x.find_all('strong')


tagextras=soup.find_all('div' ,{'id':"lp-pom-text-941"})
for x in tagextras:
      taxasextras=x.find_all('strong')


tagpreco=soup.find_all('div' ,{'id':"lp-pom-text-943"})
for x in tagpreco:
      preco=x.find_all('strong')
"""