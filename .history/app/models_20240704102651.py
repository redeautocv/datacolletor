from flask import Flask,  Blueprint 
import psycopg2
import app.controllers
import app.initi
models= Blueprint('models',__name__)
from initi import db

class anuncio (db.model):
    


try:

    conectDb = psycopg2.connect( host="localhost",
                                database="postgres",
                                port="5432",
                                user="postgres",
 
                             password="benoit")
    
except:
    print("erroooOOOOOOOOOOOOO")

print("Conectou-se caralh0")
#print("Marca",app.controllers.marcaCarro[2][0].text )
#print("Nuemro lugares",app.controllers.numeroLugares[2][0].text)
#print("Taxas Extras",app.controllers.taxasextras)
#print("Preco",app.controllers.preco) 

dataanuncio=[]

for i in range(len(app.controllers.numberannoument) ):
   # print(app.controllers.marcaCarro[i][0].text)
  #  print(app.controllers.numeroLugares[i][0].text)
  #  print(app.controllers.taxasextras[i][0].text)
  #  print(app.controllers.preco[i][0].text)
  #  print(app.controllers.numeroLugares[i][1].text)
     dataanuncio.append((app.controllers.marcaCarro[i][0].text,app.controllers.numeroLugares[i][0].text,app.controllers.taxasextras[i][0].text,app.controllers.preco[i][0].text,app.controllers.numeroLugares[i][1].text  ))



try:
    db= conectDb.cursor()
    #print(dataanuncio)
    sql='Insert into publicar (tipoCarro , numeroLugares  , taxasExtras , preco  , tipoCombustivel ) values (%s, %s, %s , %s ,%s)'
    db.executemany(sql,dataanuncio)
    conectDb.commit()
except:
    print("error database ")


# Fetch the results
#result = db.fetchone()

# Print the results
#print(result)

# Close the cursor and connection
 