from flask import jsonify
from dao import patient

class PatientHandler:

 def build_patient_dict(self, row):
        result = {}
        result['PatientID'] = row[0]
        result['PatientName']=row[1]
        result['PatientAge'] = row[2]
        result['PatientLocation'] = row[3]
        return result

 def build_patient_attributes(self, PatientID, PatientName, PatientAge, PatientLocation):
    result = {}
    result['PatientID'] = PatientID
    result['PatientName'] = PatientName
    result['PatientAge'] = PatientAge
    result['PatientLocation'] = PatientLocation
    return result

 def getAllPatients(self):
    dao = patient.PatientDAO()
    patients_list = dao.getAllPatients()
    result_list = []
    for row in patients_list:
        result = self.build_patient_dict(row)
        result_list.append(result)
    return jsonify(patients=result_list)
   
 def getPatientById(self, json):
        Id = json['Id']
        if Id:
            dao = patient.PatientDAO()
            row = dao.getPatientById(Id)
            if not row:
                return jsonify(Error = "Patient Not Found"), 404
            return jsonify(patient = "Patient Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

 def insertPatientJson(self, json):
        PatientName = json['Name']
        PatientAge = json['age']
        PatientLocation = json['location']
        if PatientAge and PatientLocation and PatientName:
            dao = patient.PatientDAO()
            PatientID = dao.insert(PatientName, PatientAge, PatientLocation)
            result = self.build_patient_attributes(PatientID, PatientName, PatientAge, PatientLocation)
            return jsonify(patient=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400



