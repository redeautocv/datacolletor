import  psycopg2

conectDb = psycopg2.connect(
        host="pgsql-server-racv.postgres.database.azure.com",
        database="flask_db",
        port='5432'
        user='psqladminun@pgsql-server-racv',
        password=os.environ['DB_PASSWORD'])
