from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from dao.doctor import DoctorDAO
from dao.patient import PatientDAO
from dao.users import UsersDAO

from handler.doctor import DoctorHandler
from handler.patient import PatientHandler
from handler.users import UsersHandler

app = Flask(__name__)
api = Api(app)
# Apply CORS to this app
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Greeting(Resource):
    def get(self):
        return 'Hello World! Welcome to MedSearch'

#GET and Insert for Doctors
class Doctor(Resource):
    dHandler = DoctorHandler()
    def get(self):
        return self.dHandler.getAllDoctors()
    # def put(self):
    #     print('req:', request.json)
    #     return self.dHandler.insertDoctorJson(request.json)

#GET and Insert for Patients
class Patient(Resource):
    pHandler = PatientHandler()
    def get(self):
        return self.pHandler.getAllPatients()
    # def put(self):
    #     print('req:', request.json)
    #     return self.pHandler.insertPatientJson(request.json)

#GET and Insert for User accounts
class User(Resource):
    uHandler = UsersHandler()
    def get(self):
        return self.uHandler.getAllUsers()
    def post(self):
        print('req:', request.json)
        res = self.uHandler.insertUsersJson(request.json)
        print(res)
        return res

#ADD the resources to the api
api.add_resource(Greeting, '/', '/home')
api.add_resource(Doctor, '/doctor')
api.add_resource(Patient, '/patient')
api.add_resource(User, '/user')


if __name__ == '__main__':
    app.run(debug=True)