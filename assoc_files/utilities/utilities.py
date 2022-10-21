import binascii
import os
from assoc_files import app
from flask import jsonify ,session , redirect,url_for
from functools import wraps
from assoc_files.entity.UserClass import User
#from assoc_files.log.logging import logger
from assoc_files.database.modal import UserTable

state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
redirect_uri = app.config["redirect_uri"]
scopes = ['read_products', 'read_orders','write_orders']
scopes_string = ','.join(scopes)

def verifyLogin(dbUser):
    if dbUser!=None:
        if dbUser.accessToken != "":
            session["accessToken"] = dbUser.accessToken
            session["logged_in"] = True
            session["userId"] = dbUser.id

            return True
        return False
    return False


def createAuthUrl():
    auth_url = f"https://{app.config['shop_url']}/admin/oauth/authorize?client_id={app.config['API_KEY']}&scope={scopes_string}&redirect_uri={app.config['redirect_uri']}&state={state}"
    return auth_url

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return decorated_function

def token_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if "accessToken" in session and session['accessToken'] != '':
            return f(*args,**kwargs)
        else:
            return redirect(url_for("getToken"))
    return decorated_function

def validate(user:User,dbUser:UserTable):
    if dbUser!= None:
        if user.email == dbUser.email:
            if user.password == dbUser.password:
                user.accessToken = dbUser.accessToken
                session["logged_in"] = True
                session["userId"] = dbUser.id
                session["accessToken"] = user.accessToken
                return True
            return False
    return False


def deleteAccessToken():
    try:
        print(session["userId"])
        #logger.info(f"UserId -> {session['userId']} called deleteAccessToken function")
        deleteToken = UserTable.query.filter_by(id=session['userId']).one_or_none()
        if deleteToken != None and deleteToken.accessToken != '':
            deleteToken.accessToken=''
            UserTable.updateTable(deleteToken)
            return True
        return False
    except Exception as e:
        return False
        #logger.error(f"Error occurred while delete accessToken error -> {e} userId -> {session['userId']}")
