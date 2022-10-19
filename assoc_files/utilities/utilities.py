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
            session["userId"] = dbUser.id

            return True
        return False
    return False



def getOrder():
    print(app.config["shop_url"])
    if app.config["shop_url"] == '' or app.config["shop_url"] == None:
        return redirect(url_for("login"))

    else:
        header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
        print(app.config['shop_url'], 'ni')
        response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders.json?financial_status:paid AND fulfillment_status:unshipped",headers=header)
        data = response.json()
        print(response.json())

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
    checkUser = UserTable.query.filter_by(shopurl=user.shopUrl).one_or_none()
    if checkUser==None:
        entity = UserTable(accessToken=user.accessToken,shopurl=user.shopUrl)
        UserTable.insert(entity)
    else:
        session["userId"] = checkUser.id
        checkUser.accessToken = user.accessToken
        UserTable.updateTable(checkUser)

def insertOrderOnDb(order:list):
    try:
        for i in range(0,len(order)):
            print(order[i].orderId,session['userId'])
            dbOrder = OrderTable(orderId=order[i].orderId,userId=session['userId'],firstName=order[i].firstName,lastName=order[i].lastName,orderStatus=order[i].orderStatus,orderName=order[i].orderName,address1=order[i].address1,phone=order[i].phone,orderDate=order[i].date,city=order[i].city,zip=order[i].zip,address2=order[i].address2,country=order[i].country,company=order[i].company,name=order[i].name,countryCode=order[i].countryCode)
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
            order.orderId = data["orders"][i]["id"]
            order.firstName = data["orders"][i]["shipping_address"]["first_name"]
            order.lastName = data["orders"][i]["shipping_address"]["last_name"]
            order.date = data["orders"][i]["created_at"]
            order.orderStatus = data["orders"][i]["fulfillment_status"]
            order.address1 = data["orders"][i]["shipping_address"]["address1"]
            order.phone = data["orders"][i]["shipping_address"]["phone"]
            order.city = data["orders"][i]["shipping_address"]["city"]
            order.zip = data["orders"][i]["shipping_address"]["zip"]
            order.country = data["orders"][i]["shipping_address"]["country"]
            order.address2 = data["orders"][i]["shipping_address"]["address2"]
            order.company = data["orders"][i]["shipping_address"]["company"]
            order.name = data["orders"][i]["shipping_address"]["name"]
            order.countryCode = data["orders"][i]["shipping_address"]["country_code"]
            order.orderName = data["orders"][i]["name"]

            if order.orderStatus == None:
                order.orderStatus = "Null"
            if order.orderName == None:
                order.orderName = "null"
            if order.company == None:
                order.company = "default"
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
