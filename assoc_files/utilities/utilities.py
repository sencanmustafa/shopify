import requests
from html5lib import serialize
from assoc_files import app
from flask import jsonify ,session , redirect,url_for
from functools import wraps
from assoc_files.entity.UserClass import Order , User
from assoc_files.log.logging import logger
from assoc_files.modal import UserTable,OrderTable
import datetime

def getOrder(url:str):
    header = {f"X-Shopify-Access-Token": session["accessToken"]}
    response = requests.get(app.config["order_url"],headers=header)
    data = response.json()
    return data


def serialize_model(model):
    return jsonify(serialize(model))

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
        if "access_token" in session:
            return f(*args,**kwargs)
        else:
            return redirect(url_for("token_page"))
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
    entity.updateUserTable()

def insertOrderOnDb(order:Order):
    dbOrder = OrderTable(userId=session['userId'],firstName=order.firstName,lastName=order.lastName,address1=order.address1,phone=order.phone,orderDate=datetime.datetime.now(),city=order.city,zip=order.zip,address2=order.address2,country=order.country,company=order.company,name=order.name,countryCode=order.countryCode)
    OrderTable.insert(dbOrder)
    logger.info(f"order inserted to db , userId -> {session['userId']} ")
    return True

def jsonToObject(data:dict,order:Order):
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
