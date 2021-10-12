import mysql.connector


class PatientDAO:

    #This is the string for connecting to a DB.
    def __init__(self): 
        user = 'admin'
        password = 'Inso4116'
        host = 'inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com'
        database = 'MedSearch'
        port = '3306'

        connection_url = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)
        self.conn = connection_url

    def getAllPatients(self):
        cursor = self.conn.cursor()
        query = "select * from Patients;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPatientById(self, id):
        cursor = self.conn.cursor()
        query = "select * from Patients Where PatientID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getPatientId(PatientName, PatientAge, PatientLocation):
        cursor = self.conn.cursor()
        query = "select PatientID from Patients where PatientName = %s and PatientAge = %s and PatientLocation = %s;"
        cursor.execute(query, (PatientName, PatientAge, PatientLocation))
        result =[]
        for row in cursor:
            result.append(row)
        return result
        

    def insert(self, PatientName, PatientAge, PatientLocation):
        cursor = self.conn.cursor()
        query = "insert into Patients(PatientName, PatientAge, PatientLocation) values (%s, %s, %s) ;"
        cursor.execute(query, (PatientName, PatientAge, PatientLocation))
        patient_id = self.getPatientId(PatientName, PatientAge, PatientLocation)
        self.conn.commit()
        return patient_id