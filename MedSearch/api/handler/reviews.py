from flask import jsonify
from dao import reviews


class ReviewsHandler:

    def build_reviews_dict(self, row):
        result = {}
        result['ReviewID'] = row[0]
        result['reviewID'] = row[1]
        result['DoctorID'] = row[2]
        result['ReviewText'] = row[3]
        result['ReviewDate'] = row[4]
        return result

    def build_reviews_attributes(self, ReviewID, reviewID, DoctorID, ReviewText, ReviewDate):
        result = {}
        result['ReviewID'] = ReviewID
        result['reviewID'] = reviewID
        result['DoctorID'] = DoctorID
        result['ReviewText'] = ReviewText
        result['ReviewDate'] = ReviewDate
        return result

    def getAllReviews(self):
        dao = reviews.ReviewsDAO()
        reviews_list = dao.getAllReviews()
        result_list = []
        for row in reviews_list:
            result = self.build_reviews_dict(row)
            result_list.append(result)
        return jsonify(reviews=result_list)

    def getReviewByDate(self, json):
        ReviewDate = json['ReviewDate']
        if ReviewDate:
            dao = reviews.ReviewsDAO()
            row = dao.getReviewByDate(ReviewDate)
            if not row:
                return jsonify(Error="Review Not Found"), 404
            return jsonify(reviews="Review Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

    def getReviewsById(self, json):
        Id = json['Id']
        if Id:
            dao = reviews.ReviewsDAO()
            row = dao.getReviewById(Id)
            if not row:
                return jsonify(Error="Review Not Found"), 404
            return jsonify(reviews="Review Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

    def insertReviewsJson(self, json):
        UserID = json['UserID']
        DoctorID = json['DoctorID']
        ReviewText = json['ReviewText']
        ReviewDate = json['ReviewDate']
        if UserID and DoctorID and ReviewText and ReviewDate:
            dao = reviews.ReviewsDAO()
            ReviewID = dao.insert(UserID, DoctorID, ReviewText, ReviewDate)
            result = self.build_reviews_attributes(ReviewID, UserID, DoctorID, ReviewText, ReviewDate)
            return result, 201
        else:
            return "Unexpected attributes in post request", 400



