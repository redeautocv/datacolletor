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
    print("ddd",app.controllers.)

 
except:
    print("errooo")

 
db= conectDb.cursor()
