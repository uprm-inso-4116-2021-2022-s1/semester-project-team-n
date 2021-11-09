import mysql.connector


class AppointmentDAO:

    # This is the string for connecting to a DB.
    def __init__(self):
        user = 'admin'
        password = 'Inso4116'
        host = 'inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com'
        database = 'MedSearch'
        port = '3306'

        connection_url = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)
        self.conn = connection_url

    def getAllAppointments(self):
        cursor = self.conn.cursor()
        query = "select * from Appointments;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAppointmentById(self, id):
        cursor = self.conn.cursor()
        query = "select * from Appointments Where AppointmentID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAppointmentByDoctorId(self, id):
        cursor = self.conn.cursor()
        query = "select * from Appointments Where DoctorID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAppointmentByUserId(self, id):
        cursor = self.conn.cursor()
        query = "select * from Appointments Where UserID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAppointmentId(self, DoctorID, UserID, AppointmentDate):
        cursor = self.conn.cursor()
        query = "select AppointmentID from Appointments where DoctorID = %s and UserID = %s and AppointmentDate;"
        cursor.execute(query, (DoctorID, UserID, AppointmentDate))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, DoctorID, UserID, AppointmentDate):
        cursor = self.conn.cursor()
        query = "insert into Appointments(DoctorID, UserID, AppointmentDate) values (%s, %s, %s) ;"
        cursor.execute(query, (DoctorID, UserID, AppointmentDate))
        appointment_id = self.getAppointmentId(DoctorID, UserID, AppointmentDate)
        self.conn.commit()
        return appointment_id