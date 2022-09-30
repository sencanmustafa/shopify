from assoc_files.modal import UserTable
from flask import session

class User:
    def __init__(self,email=None,password=None,accessToken=None):
        self.email = email
        self.password = password
        self.accessToken = accessToken
    def __str__(self):
        return f"{self.email} , {self.accessToken}"


def validate(user:User,dbUser:UserTable):
    if user.email == dbUser.email:
        if user.password == dbUser.password:
            user.accessToken = dbUser.accessToken
            session["logged_in"] = True
            session["accessToken"] = user.accessToken
            return True
        return False
    return False

def UpdatetUserOnDb(user:User):
    entity = UserTable.query.filter_by(email=user.email).first()
    entity.accessToken = user.accessToken
    entity.updateUserTable()
