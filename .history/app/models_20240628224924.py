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
    print("Conectou-se caralh0")
    print("Marca",app.controllers.marcaCarro[0])
    print("Nuemro lugares",app.controllers.numeroLugares[0].text ,app.controllers.numeroLugares[1].text)
    print("Taxas Extras",app.controllers.taxasextras[0])
    print("Preco",app.controllers.preco[0].text) 
    
except:
    print("errooo")

 
db= conectDb.cursor()
db.execute("SELECT 1;")

# Fetch the results
result = db.fetchone()

# Print the results
print(result)

# Close the cursor and connection
db.close()
conectDb.close()