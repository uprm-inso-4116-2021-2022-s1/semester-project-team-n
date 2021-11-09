from flask import jsonify
from dao import Appointment


class AppointmentHandler:

    def build_appointment_dict(self, row):
        result = {}
        result['AppointmentID'] = row[0]
        result['DoctorID'] = row[1]
        result['UserID'] = row[2]
        result['AppointmentDate'] = row[3]
        return result

    def build_appointment_attributes(self, AppointmentID, DoctorID, UserID, AppointmentDate):
        result = {}
        result['AppointmentID'] = AppointmentID
        result['DoctorID'] = DoctorID
        result['UserID'] = UserID
        result['AppointmentDate'] = AppointmentDate
        return result

    def getAllAppointments(self):
        dao = Appointment.AppointmentDAO()
        appointment_list = dao.getAllAppointments()
        result_list = []
        for row in appointment_list:
            result = self.build_appointment_dict(row)
            result_list.append(result)
        return jsonify(Appointment=result_list)

    def getAppointmentById(self, json):
        Id = json['Id']
        if Id:
            dao = Appointment.AppointmentDAO()
            row = dao.getAppointmentById(Id)
            if not row:
                return jsonify(Error="Appointment Not Found"), 404
            return jsonify(Appointment="Appointment Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

    def insertAppointmentJson(self, json):
        DoctorID = json['DoctorID']
        UserID = json['UserID']
        AppointmentDate = json['AppointmentDate']
        if UserID and AppointmentDate and DoctorID:
            dao = Appointment.AppointmentDAO()
            AppointmentID = dao.insert(DoctorID, UserID, AppointmentDate)
            result = self.build_appointment_attributes(AppointmentID, DoctorID, UserID, AppointmentDate)
            return result, 201
        else:
            return "Unexpected attributes in post request", 400



