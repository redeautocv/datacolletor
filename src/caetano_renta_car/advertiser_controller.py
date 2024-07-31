from bs4 import BeautifulSoup

message = []
adress=[]
contacts=[]
hours=[]
name = "Caetano - Cabo verde "
try:
     with open("caetano_renta_car/static/caetano_location.html", "r", encoding="utf-8") as file:
         html_content = file.read()

except:
    print("djdk")

soup_one = BeautifulSoup(html_content, 'html.parser')
tags_location=soup_one.find_all('p' ,{'class':"dealerLst__content--title"})
tags_location=soup_one.find_all('p' ,{'class':"dealerLst__contacts--text"})

for x in tags_location:
    adress.append(x.text)
    contacts.append(x.text)
    hours.append(x.text)

print(adress)