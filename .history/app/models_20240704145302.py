from flask import Flask,  Blueprint 
import psycopg2
import app.controllers
from .   import dbt

class  publicar
    models= Blueprint('models',__name__)
    tipoCarro  = dbt.Column(dbt.String(50))
    numeroLugares  = dbt.Column(dbt.String(50))
    taxasExtras = dbt.Column(dbt.String(50))
    preco=dbt.Column(dbt.String(50))

print("Conectou-se caralh0")
 
dataanuncio=[]

for i in range(len(app.controllers.numberannoument) ):
     dataanuncio.append((app.controllers.marcaCarro[i][0].text,app.controllers.numeroLugares[i][0].text,app.controllers.taxasextras[i][0].text,app.controllers.preco[i][0].text,app.controllers.numeroLugares[i][1].text  ))


try:
    db= conectDb.cursor()
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
 