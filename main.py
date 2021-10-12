from flask import Flask, request
from dao.doctor import DoctorDAO
from dao.patient import PatientDAO
from dao.users import UsersDAO
from flask_cors import CORS
from handler.doctor import DoctorHandler
from handler.patient import PatientHandler
from handler.users import UsersHandler




app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return 'Hello World! Welcome to MedSearch!'

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
    app.run()