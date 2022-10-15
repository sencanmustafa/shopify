
import requests
from html5lib import serialize
from assoc_files import app
from flask import jsonify ,session , redirect,url_for
from functools import wraps
from assoc_files.entity.UserClass import Order , User
#from assoc_files.log.logging import logger
from assoc_files.modal import UserTable,OrderTable
import datetime



def verifyLogin(dbUser):
    if dbUser!=None:
        if dbUser.accessToken != "":
            session["accessToken"] = dbUser.accessToken
            session["logged_in"] = True
            session["user_id"] = dbUser.id
            return True
        return False
    return False

def getOrder():
    header = {f"X-Shopify-Access-Token": session["accessToken"],"Content-Type": "application/json" }
    response = requests.get(app.config["order_url"],headers=header)
    data = response.json()
    print(len(data["orders"]))
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

def InsertUserOnDb(user:User):
    entity = UserTable(accessToken=user.accessToken,shopurl=user.shopUrl)
    UserTable.insert(entity)

def insertOrderOnDb(order:Order):
    try:
        dbOrder = OrderTable(userId=session['userId'],firstName=order.firstName,lastName=order.lastName,address1=order.address1,phone=order.phone,orderDate=datetime.datetime.now(),city=order.city,zip=order.zip,address2=order.address2,country=order.country,company=order.company,name=order.name,countryCode=order.countryCode)
        OrderTable.insert(dbOrder)
        #logger.info(f"order inserted to db , userId -> {session['userId']} ")
        return True
    except Exception as e:
        print(e)
        return False
def jsonToOrder(data:dict):
    try:
        orderList = []
        for i in range(0,len(data["orders"])):
            order = Order()
            order.firstName = data["orders"][i]["shipping_address"]["first_name"]
            order.lastName = data["orders"][i]["shipping_address"]["last_name"]
            order.address1 = data["orders"][i]["shipping_address"]["address1"]
            order.phone = data["orders"][i]["shipping_address"]["phone"]
            order.city = data["orders"][i]["shipping_address"]["city"]
            order.zip = data["orders"][i]["shipping_address"]["zip"]
            order.country = data["orders"][i]["shipping_address"]["country"]
            order.address2 = data["orders"][i]["shipping_address"]["address2"]
            order.company = data["orders"][i]["shipping_address"]["company"]
            if order.company == None:
                order.company = "default"
            order.name = data["orders"][i]["shipping_address"]["name"]
            order.countryCode = data["orders"][i]["shipping_address"]["country_code"]
            orderList.append(order)
        return orderList
    except Exception as e:
        #logger.error(f"error occurred error -> {e} , userId -> {session['userId']}")
        return False

def getOrderOnDb():
    order = OrderTable.query.filter_by(userId=session['userId']).all()
    return order

def deleteAccessToken():
    try:
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
