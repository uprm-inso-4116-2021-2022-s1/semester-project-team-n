import mysql.connector


class ReviewsDAO:

    # This is the string for connecting to a DB.
    def __init__(self):
        review = 'admin'
        password = 'Inso4116'
        host = 'inso-databse.c7sgroillrv6.us-east-2.rds.amazonaws.com'
        database = 'MedSearch'
        port = '3306'

        connection_url = mysql.connector.connect(review=review, password=password, host=host, database=database, port=port)
        self.conn = connection_url

    def getAllReviews(self):
        cursor = self.conn.cursor()
        query = "select * from Reviews;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReviewById(self, id):
        cursor = self.conn.cursor()
        query = "select * from Reviews Where ReviewID = %s;"
        cursor.execute(query, (id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReviewByDate(self, ReviewDate):
        cursor = self.conn.cursor()
        query = "select * from Reviews Where ReviewDate = %s;"
        cursor.execute(query, (ReviewDate))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReviewId(self, UserID, DoctorID):
        cursor = self.conn.cursor()
        query = "select ReviewID from Reviews where UserID = %s and DoctorID = %s;"
        cursor.execute(query, (UserID, DoctorID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, UserID, DoctorID, ReviewText, ReviewDate):
        cursor = self.conn.cursor()
        query = "insert into Reviews(UserID, DoctorID, ReviewText, ReviewDate) values (%s, %s, %s. %s) ;"
        cursor.execute(query, (UserID, DoctorID, ReviewText, ReviewDate))
        review_id = self.getReviewId(UserID, DoctorID)
        self.conn.commit()
        return review_id