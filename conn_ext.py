import psycopg2

#for database connection
DB_NAME = "inventorysystem"
DB_USER = "postgres"
DB_PASS = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)

cur = conn.cursor()

print("Database connected!")

    