import mysql.connector


class UsersDAO:

    #This is the string for connecting to a DB.
    def __init__(self):
        user = 'admin'
        password = 'Inso4116'
        host = 'inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com'
        database = 'MedSearch'
        port = '3306'

        connection_url = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)
        self.conn = connection_url

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, id):
        cursor = self.conn.cursor()
        query = "select * from Users Where UserID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getUserId(self, email, password):
        cursor = self.conn.cursor()
        query = "select UserID from Users where email = %s and password = %s;"
        cursor.execute(query, (email, password))
        result =[]
        for row in cursor:
            result.append(row)
        return result
        

    def insert(self, Email, Password, AccountType):
        cursor = self.conn.cursor()
        query = "insert into Users(Email, Password, AccountType) values (%s, %s, %s) ;"
        cursor.execute(query, (Email, Password, AccountType))
        user_id = self.getUserId(Email, Password)
        self.conn.commit()
        return user_id