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
   # print("Conectou-se caralh0")
   # print("Marca",app.controllers.marcaCarro)
   # print("Nuemro lugares",app.controllers.numeroLugares)
   # print("Taxas Extras",app.controllers.taxasextras)
    print("Preco",app.controllers.x) 
    
except:
    print("errooo")

 
db= conectDb.cursor()
