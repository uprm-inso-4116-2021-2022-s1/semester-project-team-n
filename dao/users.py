import psycopg2


class UsersDAO:

    #This is the string for connecting to a DB.
    def __init__(self):
        connection_url = psycopg2.connect(host='inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com',
                                          user='admin',
                                          password='Inso4116',
                                          dbname='MedSearch', port=3360)
        self.conn = connection_url

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, id):
        cursor = self.conn.cursor()
        query = "select * from users Where UserID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getUserId(email, password):
        cursor = self.conn.cursor()
        query = "select UserID from users where email = %s and password = %s;"
        cursor.execute(query, (email, password))
        result =[]
        for row in cursor:
            result.append(row)
        return result
        

    def insert(self, Email, Password, AccountID):
        cursor = self.conn.cursor()
        query = "insert into users(Email, Password, AccountID) values (%s, %s, %s) ;"
        cursor.execute(query, (Email, Password, AccountID))
        user_id = self.getUserId(Email, Password, AccountID)
        self.conn.commit()
        return user_id