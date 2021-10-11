import mysql.connector

user = 'admin'
password = 'Inso4116'
host = 'inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com'
database = 'MedSearch'
port = '3306'

db = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

print("Connected to database!")

cursor = db.cursor(buffered=True)

query = ("SHOW Tables;")

cursor.execute(query)

tables = cursor.fetchall()

print(tables)

cursor.close()

db.close()