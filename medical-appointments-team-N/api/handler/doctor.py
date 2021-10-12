from flask import jsonify
from dao import doctor

class DoctorHandler:

 def build_doctor_dict(self, row):
        result = {}
        result['DoctorID'] = row[0]
        result['DoctorName']=row[1]
        result['DoctorType'] = row[2]
        result['DoctorLocation'] = row[3]
        return result

 def build_doctor_attributes(self, DoctorID, DoctorName, DoctorType, DoctorLocation):
    result = {}
    result['DoctorID'] = DoctorID
    result['DoctorName'] = DoctorName
    result['DoctorType'] = DoctorType
    result['DoctorLocation'] = DoctorLocation
    return result

 def getAllDoctors(self):
    dao = doctor.DoctorDAO
    doctors_list = dao.getAllDoctors()
    result_list = []
    for row in doctors_list:
        result = self.build_doctor_dict(row)
        result_list.append(result)
    return jsonify(doctors=result_list)
   
 def getDoctorByLocation(self, json):
        location = json['Location']
        if location:
            dao = doctor.DoctorDAO()
            row = dao.getDoctorByLocation(location)
            if not row:
                return jsonify(Error = "Doctor Not Found"), 404
            return jsonify(doctor = "Doctor Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

 def insertDoctorJson(self, json):
        DoctorName = json['DoctorName']
        DoctorType = json['DoctorType']
        DoctorLocation = json['DoctorLocation']
        if DoctorType and DoctorLocation and DoctorName:
            dao = doctor.DoctorDAO()
            DoctorID = dao.insert(DoctorName, DoctorType, DoctorLocation)
            result = self.build_doctor_attributes(DoctorID, DoctorName, DoctorType, DoctorLocation)
            return jsonify(doctor=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400



