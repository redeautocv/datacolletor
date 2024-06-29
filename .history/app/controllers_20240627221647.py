import requests
from bs4 import BeautifulSoup

URL = "https://caetano.cv/rent-a-car/"  
 

response = requests.get(URL)
conteudo = response.text
 

soup = BeautifulSoup(conteudo, 'html5lib')

tituloNoticia=soup.find_all('h3',{'class':'title'})
dataNoticia=soup.find_all('span',{'class':'pubdate'})
subtituloNoticia=soup.find_all('p',{'class':'summary'})
tagImagemNoticia=soup.find_all('div', {'class':'col-md-4 featuredThumb'})
imagemNoticia=soup.find_all('img')