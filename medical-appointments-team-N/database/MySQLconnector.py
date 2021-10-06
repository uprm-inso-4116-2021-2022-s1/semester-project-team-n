import mysql.connector

user = 'admin'
password = 'Inso4116'
host = 'inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com'
database = 'doctor_data'
port = '3306'

db = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

print("Connected to database!")

db.close()