import psycopg2


class PatientDAO:

    #This is the string for connecting to a DB.
    def __init__(self):
        connection_url = psycopg2.connect(host='inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com',
                                          user='admin',
                                          password='Inso4116',
                                          dbname='MedSearch', port=3360)
        self.conn = connection_url

    def getAllPatients(self):
        cursor = self.conn.cursor()
        query = "select * from patients;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPatientById(self, id):
        cursor = self.conn.cursor()
        query = "select * from patients Where PatientID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getPatientId(PatientName, PatientAge, PatientLocation):
        cursor = self.conn.cursor()
        query = "select PatientID from patients where PatientName = %s and PatientAge = %s and PatientLocation = %s;"
        cursor.execute(query, (PatientName, PatientAge, PatientLocation))
        result =[]
        for row in cursor:
            result.append(row)
        return result
        

    def insert(self, PatientName, PatientAge, PatientLocation):
        cursor = self.conn.cursor()
        query = "insert into patients(PatientName, PatientAge, PatientLocation) values (%s, %s, %s) ;"
        cursor.execute(query, (PatientName, PatientAge, PatientLocation))
        patient_id = self.getPatientId(PatientName, PatientAge, PatientLocation)
        self.conn.commit()
        return patient_id