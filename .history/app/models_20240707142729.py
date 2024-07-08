from flask import Flask,  Blueprint 
import psycopg2
from .   import dbt

class  publicar(dbt.Model):
    id = dbt.Column(dbt.String(50), primary_key=True, nullable=False, unique=True)
    tipocarro  = dbt.Column(dbt.String(50))
    numerolugares  = dbt.Column(dbt.String(50))
    taxasextras = dbt.Column(dbt.String(50))
    preco=dbt.Column(dbt.String(50))
    
    def todict():
        return
        {
            "tipo de carrro":
            "Numero de lugares":
            "taxa extras":
            "preco "
        }

""" 
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

"""
# Fetch the results
#result = db.fetchone()
# Print the results
#print(result)
# Close the cursor and connection
 