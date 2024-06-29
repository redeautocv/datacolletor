import  psycopg2

conectDb = psycopg2.connect(
        host="pgsql-server-racv.postgres.database.azure.com",
        database="flask_db",
        port=
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
