from flask import jsonify
from dao import users

class UsersHandler:

 def build_users_dict(self, row):
        result = {}
        result['UserID'] = row[0]
        result['Email']=row[1]
        result['Password'] = row[2]
        result['AccountType'] = row[3]
        return result

 def build_users_attributes(self, UserID, Email, Password, AccountType):
    result = {}
    result['UserID'] = UserID
    result['Email'] = Email
    result['Password'] = Password
    result['AccountType'] = AccountType
    return result

 def getAllUsers(self):
    dao = users.UsersDAO()
    users_list = dao.getAllUsers()
    result_list = []
    for row in users_list:
        result = self.build_users_dict(row)
        result_list.append(result)
    return jsonify(users=result_list)
   
 def getUsersById(self, json):
        Id = json['Id']
        if Id:
            dao = users.UsersDAO()
            row = dao.getUserById(Id)
            if not row:
                return jsonify(Error = "User Not Found"), 404
            return jsonify(users = "User Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

 def insertUsersJson(self, json):
        Email = json['Email']
        Password = json['Password']
        AccountType = json['AccountType']
        if Password and AccountType and Email:
            dao = users.UsersDAO()
            UserID = dao.insert(Email, Password, AccountType)
            result = self.build_users_attributes(UserID, Email, Password, AccountType)
            return result, 201
        else:
            return "Unexpected attributes in post request", 400



