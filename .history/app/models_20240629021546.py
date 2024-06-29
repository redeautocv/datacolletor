from flask import Flask,  Blueprint
import psycopg2
import app.controllers
models= Blueprint('models',__name__)

try:

    conectDb = psycopg2.connect( host="pgsql-server-racv.postgres.database.azure.com",
                                database="racvdb",
                                port='5432',
                                user="psqladminun@pgsql-server-racv",
 
                             password="H@camelo!")
    
except:
    print("errooo")

print("Conectou-se caralh0")
print("Marca",app.controllers.marcaCarro )
print("Nuemro lugares",app.controllers.numeroLugares)
print("Taxas Extras",app.controllers.taxasextras)
print("Preco",app.controllers.preco[12][0].text) 

dataanuncio=[]
""""""
for i in range(13):
    tipocarro=app.controllers.marcaCarro[i].text
    numeroLugar=numeroLugares[i][0].text
    extras=app.controllers.taxasextras[0]
    price=app.controllers.preco[i][0].text
    combustivel=app.controllers.numeroLugares[i][0].text
    
    dataanuncio.append(( tipocarro,numeroLugar,extras,price,combustivel  ))
 

db= conectDb.cursor()
print(dataanuncio)
#db.execute('Insert into publicar (tipoCarro , numeroLugares  , taxasExtras , preco  , tipoCombustivel ) values (%s, %s, %s , %s ,%s) , ')

# Fetch the results
result = db.fetchone()

# Print the results
print(result)

# Close the cursor and connection
db.close()
conectDb.close()