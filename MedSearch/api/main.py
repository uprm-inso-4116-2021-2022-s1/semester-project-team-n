from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource

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

#Get and Insert for Doctors

#Get and Insert for Patients

#Get and Insert for User accounts

api.add_resource(Greeting, '/', '/home')

# Get and Insert for Doctors
@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return DoctorHandler().insertDoctorJson(request.json)
    else:
        if not request.args:
            return DoctorHandler().getAllDoctors()

# Get and Insert for Patients
@app.route('/patient', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PatientHandler().insertPatientJson(request.json)
    else:
        if not request.args:
            return PatientHandler().getAllPatients()

# Get and Insert for Users(accounts)
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUsersJson(request.json)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()


if __name__ == '__main__':
    app.run(debug=True)