from bs4 import BeautifulSoup
from .advertiser_controller import adress

TOTAL_ANUNCIOS =0
marca_carro = []
numero_lugares = []
taxas_extras = []   
preco = []
intervalo = []
message=[]
listings=[]
locations=[]
ads=[]
dati=[]
# Leitura dos arquivos HTML
#/mnt/c/Users/HP/Documents/datacolletor/src/Announcement
with open("caetano_renta_car/static/Rent-a-Car _ Caetano Cabo Verde.html", "r", encoding="utf-8") as file:
    html_content = file.read()

with open("caetano_renta_car/static/caetano_cabo Verde.html", "r", encoding="utf-8") as file:
    html_content_one = file.read()

# Parsing dos arquivos HTML
soup = BeautifulSoup(html_content, 'html.parser')
soup_one = BeautifulSoup(html_content_one, 'html.parser')

# Extração de tags relevantes
tags_sites = soup.find_all('div', {'class': "lp-element lp-pom-box"})
tagsSites_Message=soup.find('p' ,{'class':"header--text"})
tag_m = soup_one.find('p',{'class':'header--text'})
message.append(tag_m.text)
def intervalo_anuncio(intervalos):
    tags_anuncio = []
    for intervalo in intervalos:
        tags_anuncio.append(intervalo.split("-"))
    return tags_anuncio

def anuncios_reais(tags_subdivididas):
    numeros = []
    for tag in tags_subdivididas:
        if tag[3].isdigit():
            num = int(tag[3])
            if 913 <= num <= 1151:
                numeros.append(num)
    return numeros

# Extração dos intervalos
for tag in tags_sites:
    intervalo.append(tag['id'])

# Processamento dos intervalos
tags_subdivididas = intervalo_anuncio(intervalo)
number_announcement = anuncios_reais(tags_subdivididas)

# Extração dos dados de interesse
for num in number_announcement:
    tag_nome = soup.find_all('div', {'id': "lp-pom-text-" + str(num + 2)})
    for tag in tag_nome:
        marca_carro.append(tag.find_all('strong'))
        TOTAL_ANUNCIOS= TOTAL_ANUNCIOS + 1
                    
    tag_lugares = soup.find_all('div', {'id': "lp-pom-text-" + str(num + 3)})
    for tag in tag_lugares:
        numero_lugares.append(tag.find_all('strong'))

    tag_extras = soup.find_all('div', {'id': "lp-pom-text-" + str(num + 4)})
    for tag in tag_extras:
        taxas_extras.append(tag.find_all('span', style=True))

    tag_preco = soup.find_all('div', {'id': "lp-pom-text-" + str(num + 6)})
    for tag in tag_preco:
        preco.append(tag.find_all('strong'))

message.append(tagsSites_Message)


#estilizar codigo para envio json
for  lista  in range(0,TOTAL_ANUNCIOS):
    listing= { "listings":[
            {"brand": marca_carro[lista][0].text},  
            {"passenger_number":numero_lugares[lista][0].text },
            {"price":preco[lista][0].text},
            {"extra_fees":taxas_extras[lista][0].text },
            {"fuel_type":numero_lugares[lista][1].text}
        ]
    }
    listings.append(listing)

for  number  in range(0,12,3):
    location= { "locations":[
             {"county": adress[number+1]}
         ]  
     }
    locations.append(location)

for  nume  in range(1,12,3):
    ad={ "advertisers": [
          {"contact": adress [nume]} ,
          {"company_name": "Caetano Cabo verde"}  
        ]
    }
    ads.append(ad)

dati.append(ads)
dati.append(locations)
dati.append(listings)

# Print (opcional) para verificar os resultados
#print(marca_carro)
#print(numero_lugares)
#print(taxas_extras)
#print(preco)
print("Olime porra",dati)
