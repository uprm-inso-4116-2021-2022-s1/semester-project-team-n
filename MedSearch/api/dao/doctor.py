import mysql.connector


class DoctorDAO:

    #This is the string for connecting to a DB.
    def __init__(self):
        user = 'admin'
        password = 'Inso4116'
        host = 'inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com'
        database = 'MedSearch'
        port = '3306'

        connection_url = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)
        self.conn = connection_url

    def getAllDoctors(self):
        cursor = self.conn.cursor()
        query = "select * from Doctors;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoctorByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from Doctors Where DoctorLocation = %s;"
        cursor.execute(query, (location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoctorId(self, DoctorName, DoctorType, DoctorLocation):
        cursor = self.conn.cursor()
        query = "select DoctorID from Doctors where DoctorName = %s and DoctorType = %s and DoctorLocation = %s;"
        cursor.execute(query, (DoctorName, DoctorType, DoctorLocation))
        result =[]
        for row in cursor:
            result.append(row)
        return result

    def insert(self, DoctorName, DoctorType, DoctorLocation):
        cursor = self.conn.cursor()
        query = "insert into Doctor(DoctorName, DoctorType, DoctorLocation) values (%s, %s, %s) ;"
        cursor.execute(query, (DoctorName, DoctorType, DoctorLocation))
        doctor_id = self.getDoctorId(DoctorName, DoctorType, DoctorLocation)
        self.conn.commit()
        return doctor_id