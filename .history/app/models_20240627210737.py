from flask import Flask,  Blueprint
import psycopg2

models= Blueprint('models',__name__)

try:

    conectDb = psycopg2.connect( host="pgsql-server-racv.postgres.database.azure.com",
                                database="racvdb",
                                port='5432',
                                user="psqladminun@pgsql-server-racv",
                                password="H@camelo!")
    print("Conectou-se caralh0")

except:
    print("errooo")


db= conectDb.cursor()
db.execute( 'CREATE TABLE carro(FORNECEDOR INT,FOTOGRAFIA VARCHAR(45),NUMERO_PASSAGEIRO INT,MARCA VARCHAR(45),MODELO VARCHAR(45),PRECO DOUBLE,CAIXA_VELOCIDADE VARCHAR(45),NUMERO_PORTAS INT, AR_CONDICIONADO VARCHAR(45),DATA_DISPONIVEL DATE,TIPO_COMBUSTIVEL VARCHAR(45),
    KILOMETRAGEM INT,
    QUANTIDADE_COMBUSTIVEL INT,
    GPS CHAR(1),
    TAXAS_EXTRAS DOUBLE,
    ANO_FABRICACAO DATE,
    DISPONIVEL CHAR(1),
    T_ANUNCIANTE_ID_ANUNCIANTE INT,
    T_ANUNCIANTE_ID_LOCALIZACAO INT,
    )  )