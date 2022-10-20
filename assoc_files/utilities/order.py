import requests
from assoc_files import app
from flask import session, redirect, url_for,flash
from assoc_files.entity.UserClass import User,Order
from assoc_files.modal import OrderTable, UserTable


def getOrder():
    print(app.config["shop_url"])
    if app.config["shop_url"] == '' or app.config["shop_url"] == None:
        return redirect(url_for("login"))
    else:
        header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
        response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders.json?financial_status:paid AND fulfillment_status:unshipped",headers=header)
        data = response.json()
        return data



def updateShopifyOrder(orderId,address):
    if app.config["shop_url"] == '' or app.config["shop_url"] == None:
        flash(message="hata")
        return False
    headers = {f"X-Shopify-Access-Token":session["accessToken"]}

    json_data = {
        'order': {
            'id': orderId,
            'tags':'Adres Duzenlendi',
            'shipping_address': {
                'address1': address
            },
        },
    }

    response = requests.put(f"https://{app.config['shop_url']}/admin/api/2022-07/orders/{orderId}.json",headers=headers, json=json_data)
    if response.status_code == 200:
        return True
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