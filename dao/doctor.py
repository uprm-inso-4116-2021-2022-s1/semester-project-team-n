import psycopg2


class DoctorDAO:

    #This is the string for connecting to a DB.
    def __init__(self):
        connection_url = psycopg2.connect(host='inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com',
                                          user='admin',
                                          password='Inso4116',
                                          dbname='MedSearch', port=3360)
        self.conn = connection_url

    def getAllDoctors(self):
        cursor = self.conn.cursor()
        query = "select * from doctors;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoctorByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from doctors Where DoctorLocation = %s;"
        cursor.execute(query, (location))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoctorId(DoctorName, DoctorType, DoctorLocation):
        cursor = self.conn.cursor()
        query = "select DoctorID from doctors where DoctorName = %s and DoctorType = %s and DoctorLocation = %s;"
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