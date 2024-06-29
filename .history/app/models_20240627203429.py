from flask import 
import  psycopg2

try:

    conectDb = psycopg2.connect( host="pgsql-server-racv.postgres.database.azure.com",
                                database="racvdb",
                                port='5432',
                                user="psqladminun@pgsql-server-racv",
                                password="H@camelo!")
    print("Conectou-se caralh0")
except:
    print("errooo")
