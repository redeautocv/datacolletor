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
    print("Marca",app.controllers.marcaCarro)
    print("Marca",app.controllers.numeroLugares)
    print("Marca",app.controllers.ta)
    print("Marca",app.controllers.marcaCarro)


 
except:
    print("errooo")

 
db= conectDb.cursor()
