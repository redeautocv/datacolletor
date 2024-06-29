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


def intervaloAnuncio (intervalos):
    tagsAnunco=[]
    for i  in range(len(intervalos)):
              tagsAnunco.append(intervalos[i].split("-"))
    
    return tagsAnunco


def anunciosReais (tagSubdivididas):
    tagsAnunco=[]
    numeros=[]
    for i  in range(len(tagSubdivididas)):
            if tagSubdivididas[i][3].isdigit():
                    num = int(tagSubdivididas[i][3])
                    if  ((num >= 913) and (num <= 1131)):
                                num,          
 
 


for y in tagsSites:
    intervalo.append(y['id'])
    
x=intervaloAnuncio (intervalo)
anunciosReais (x)



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