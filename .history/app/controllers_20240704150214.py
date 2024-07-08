import requests
from bs4 import BeautifulSoup
from .
#URL = "https://caetano.cv/rent-a-car/"  
#response = requests.get(URL)


with open("C:/Users/HP/Documents/datacolletor/app/Rent-a-Car _ Caetano Cabo Verde.html", "r", encoding="utf-8") as file:
    html_content = file.read()

#conteudo = response.text
soup = BeautifulSoup(html_content, 'html.parser')
 
marcaCarro=[]
numeroLugares=[]
taxasextras=[]
preco=[]
intervalo=[]

#soup = BeautifulSoup(conteudo, 'html5lib')
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
                    if  ((num >= 913) and (num <= 1151)):
                                numeros.append(num) 

    return  numeros
 


for y in tagsSites:
    intervalo.append(y['id'])
    
x=intervaloAnuncio (intervalo)
numberannoument=anunciosReais (x)


for i in range(len(numberannoument)):

    tagnome=soup.find_all('div' ,{'id':"lp-pom-text-"+str(numberannoument[i]+2)})
    for x in tagnome:
        marcaCarro.append(x.find_all('strong'))
                    
    taglugares=soup.find_all('div' ,{'id':"lp-pom-text-"+str(numberannoument[i]+3)})
    for x in taglugares:
        numeroLugares.append(x.find_all('strong'))

    tagextras=soup.find_all('div' ,{'id':"lp-pom-text-"+str(numberannoument[i]+4)})
    for x in tagextras:
        taxasextras.append(x.find_all('span', style=True))

        
    tagpreco=soup.find_all('div' ,{'id':"lp-pom-text-"+str(numberannoument[i]+6)})
    for x in tagpreco:
        preco.append(x.find_all('strong'))



 