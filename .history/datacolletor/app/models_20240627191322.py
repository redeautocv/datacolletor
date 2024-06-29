import  psycopg2

conectDb = psycopg2.connect(
        host="https://pgsql-server-racv.postgres.database.azure.com",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
