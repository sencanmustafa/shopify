import json
import requests
from html5lib import serialize
from assoc_files import app
from flask import jsonify ,session , redirect,url_for
from functools import wraps
from assoc_files.entity.UserClass import Order , User
from assoc_files.log.logging import logger
from assoc_files.modal import UserTable,OrderTable
import datetime
import ast




def getOrder():
    header = {f"X-Shopify-Access-Token": session["accessToken"],"Content-Type": "application/json" }
    response = requests.get(app.config["order_url"],headers=header)
    data = response.json()

    #####ERROR
    return data

def serialize_model(model):
    return jsonify(serialize(model,encoding='utf-8'))

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

def UpdatetUserOnDb(user:User):
    entity = UserTable.query.filter_by(email=user.email).first()
    entity.accessToken = user.accessToken
    UserTable.updateTable(entity)

def insertOrderOnDb(order:Order):
    dbOrder = OrderTable(userId=session['userId'],firstName=order.firstName,lastName=order.lastName,address1=order.address1,phone=order.phone,orderDate=datetime.datetime.now(),city=order.city,zip=order.zip,address2=order.address2,country=order.country,company=order.company,name=order.name,countryCode=order.countryCode)
    OrderTable.insert(dbOrder)
    logger.info(f"order inserted to db , userId -> {session['userId']} ")
    return True

def jsonToOrder(data:dict,order:Order):
    try:
        order.firstName = data["first_name"]
        order.lastName = data["last_name"]
        order.address1 = data["address1"]
        order.phone = data["phone"]
        order.city = data["city"]
        order.zip = data["zip"]
        order.country = data["country"]
        order.address2 = data["address2"]
        order.company = data["company"]
        order.name = data["name"]
        order.countryCode = data["country_code"]
        return order
    except Exception as e:
        logger.error(f"error occurred error -> {e} , userId -> {session['userId']}")
        return False

def getOrderOnDb():
    order = OrderTable.query.filter_by(userId=session['userId']).all()
    return order

def deleteAccessToken():
    try:
        logger.info(f"UserId -> {session['userId']} called deleteAccessToken function")
        deleteToken = UserTable.query.filter_by(id=session['userId']).one_or_none()
        if deleteToken != None and deleteToken.accessToken != '':
            deleteToken.accessToken=''
            UserTable.updateTable(deleteToken)
            return True
        return False
    except Exception as e:
        logger.error(f"Error occurred while delete accessToken error -> {e} userId -> {session['userId']}")
