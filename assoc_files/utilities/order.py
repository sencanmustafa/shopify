import time

from assoc_files.utilities.utilities import urlRequired
from assoc_files import app
from flask import session,flash
from barcode.writer import ImageWriter
import barcode
from assoc_files.yurticiApi.cargoApi import *


##### JSON DATA TO SEND SHOPIFY IN REQUEST #####
def jsonData(orderId,tag,address=None):
    if address !=None:
        json_data = {'order': {'id': orderId,'tags':tag,'shipping_address': {'address1': address},},}
    else:
        json_data = {'order': {'id': orderId, 'tags': tag}, }
    return json_data


##### JSON DATA TO SEND SHOPIFY IN REQUEST #####






###### CHECK SHOP URL ######

def checkSessionUrl():
    if app.config['shop_url'] == '' or app.config['shop_url'] == None:
        flash(message="hata")
        return False
    return True

###### CHECK SHOP URL ######



####### FULFILLMENT #######

def fulFillment():
    try:
        checkSessionUrl()
        db_orders = OrderTable.query.filter_by(userId=session["userId"],orderStatus=3).all()
        headers = {f"X-Shopify-Access-Token": session["accessToken"],"Content-Type": "application/json"}
        for i in db_orders:
            response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders/{int(i.orderId)}/fulfillment_orders.json",headers=headers)
            response = response.json()
            for x in range(0,len(response["fulfillment_orders"])):

                if response["fulfillment_orders"][x]["status"] == "open":
                    fulFillId = response["fulfillment_orders"][x]["line_items"][0]["fulfillment_order_id"]
                    json_data = {"fulfillment":
                                     {"message":"Siparişiniz Kargoya Teslim Edildi.","notify_customer":"False","tracking_info":
                                         {
                                             "number":i.trackingNumber,"url":i.cargoUrl,"company":"Yurtiçi Kargo"},
                                              "line_items_by_fulfillment_order":
                                                  [
                                                      {"fulfillment_order_id":fulFillId}]}}

                    response2 = requests.post("https://armonika.myshopify.com/admin/api/2022-07/fulfillments.json",headers=headers,json=json_data).json()
                    print("basarili")
                    dbUpdatedOrder = OrderTable.query.filter_by(orderId=i.orderId).first()
                    dbUpdatedOrder.orderStatus = 4
                    OrderTable.updateTable(dbUpdatedOrder)

    except Exception as e:
        print(e)
        return False

####### FULFILLMENT #######



####    SHIPPING    ####


def sendTagShipping(orderId):
    checkSessionUrl()
    headers = {f"X-Shopify-Access-Token":session["accessToken"]}
    json_data = jsonData(orderId=orderId,tag='Dagitima Cikti')
    response = requests.put(f"https://{app.config['shop_url']}/admin/api/2022-07/orders/{orderId}.json",headers=headers, json=json_data)
    if response.status_code == 200:
        return True
    return False


####    SHIPPING   #####

#####     barcode #####

def writeBarcode(orderList:list):
    try:
        for i in orderList:
            Code128 = barcode.get_barcode_class('code128')
            qr = Code128(f"{i.orderId}", writer=ImageWriter())
            qr.save(f"assoc_files/static/barcode/{i.orderId}")
        return True
    except Exception as e:
        print(e)
        return False

####      barcode ####



# UPDATE ORDER ADDRESS #
def sendTagUpdateOrderAddress(orderId,address):
    checkSessionUrl()
    headers = {f"X-Shopify-Access-Token":session["accessToken"]}

    json_data = jsonData(orderId=orderId,tag='Adres Duzenlendi',address=address)

    response = requests.put(f"https://{app.config['shop_url']}/admin/api/2022-07/orders/{orderId}.json",headers=headers, json=json_data)
    if response.status_code == 200:
        updateOrder(orderId=orderId,orderstatusStr="Adres Duzenlendi",orderStatus=0)
        time.sleep(5)
        return True
    return False
# UPDATE ORDER ADDRESS #


#  QR  #
def sendTagPrintQr(orderId):
    checkSessionUrl()
    headers = {f"X-Shopify-Access-Token":session["accessToken"]}

    json_data = jsonData(orderId=orderId,tag='Barkod Alindi')

    response = requests.put(f"https://{app.config['shop_url']}/admin/api/2022-07/orders/{orderId}.json",headers=headers, json=json_data)
    if response.status_code == 200:
        updateOrder(orderId=orderId, orderstatusStr="Barkod Alindi",orderStatus=1)
        time.sleep(5)
        return True
    return False
def callQrOrder():
    print(app.config['shop_url'])
    checkSessionUrl()
    header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
    response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders.json?financial_status:paid&fulfillment_status:unshipped&tag=Barkod Alindi",headers=header)
    data = response.json()
    return data

#  QR  #


# CARGO #
def sendTagCargo(orderId):
    #kargo islemleri
    checkSessionUrl()
    ####  SEND CARGO TO YURTICI   ####

    #if createShipment(userYurtici=callYurticiUser(), order=getOrderOnDb(orderId=orderId))==False:
    #    return False
    #if testCreateShipment(orderId=orderId) == False:
    #    return False



    ####  SEND CARGO TO YURTICI   ####
    updateOrder(orderId=orderId, orderstatusStr="Yurtici Veri Gonderildi",orderStatus=2)
    ####  SEND CARGO TO YURTICI   ####
    headers = {f"X-Shopify-Access-Token":session["accessToken"]}

    json_data = jsonData(orderId=orderId,tag='Kargoya Veri Gonderildi')

    response = requests.put(f"https://{app.config['shop_url']}/admin/api/2022-07/orders/{orderId}.json",headers=headers, json=json_data)
    if response.status_code == 200:
        updateOrder(orderId=orderId, orderstatusStr="Yurtici ve shopify veri Gonderildi",orderStatus=2)
        time.sleep(5)
        return True
    return False

def callCargoOrder():
    print(app.config['shop_url'])
    checkSessionUrl()
    header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
    response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders.json?financial_status:paid AND fulfillment_status:unshipped&tag=Kargoya Veri Gonderildi",headers=header)
    data = response.json()
    return data

# CARGO #

##### SHIPPING #####
def callShippingOrder():
    checkSessionUrl()
    header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
    response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders.json?financial_status:paid AND fulfillment_status:shipped&tag=Kargo Teslimattadır",headers=header)
    data = response.json()
    return data





##### SHIPPING #####

# NEW ORDER  #


def callNewOrder():
    print(app.config['shop_url'])
    checkSessionUrl()

    header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
    response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders.json?financial_status:paid AND fulfillment_status:unshipped",headers=header)
    data = response.json()
    return data

# NEW ORDER  #
def updateOrder(orderId,orderstatusStr:str,orderStatus:int):
    try:
        update = OrderTable.query.filter_by(orderId=orderId).one_or_none()
        if update == None:
            return False
        update.orderStatus2 = orderstatusStr
        update.orderStatus = orderStatus
        OrderTable.updateTable(update)
        return True
    except Exception as e:
        print(e)
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
            dbOrder = OrderTable(orderId=order[i].orderId,userId=session['userId'],firstName=order[i].firstName,lastName=order[i].lastName,orderStatus=order[i].orderStatus,orderName=order[i].orderName,address1=order[i].address1,phone=order[i].phone,orderDate=order[i].date,city=order[i].city,zip=order[i].zip,address2=order[i].address2,country=order[i].country,company=order[i].company,name=order[i].name,countryCode=order[i].countryCode)
            OrderTable.insert(dbOrder)
        #logger.info(f"order inserted to database , userId -> {session['userId']} ")
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
            order.fulfillment_status = data["orders"][i]["fulfillment_status"]
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
            order.tag = data["orders"][i]["tags"]
            order.orderStatusStr = "Null"

            """BAD CODE"""

            if order.fulfillment_status == None:
                order.fulfillment_status = "Null"
            if order.orderName == None:
                order.orderName = "null"
            if order.company == None:
                order.company = "default"
            if order.zip == None:
                order.zip = "default"
            if order.city == None:
                order.city = "Null"
            if order.country == None:
                order.country = "Null"
            if order.address2 == None:
                order.address2 = "Null"
            if order.name == None:
                order.name = "Null"
            if order.countryCode == None:
                order.countryCode = "Null"
            if order.date == None:
                order.date = "Null"
            if order.phone == None:
                order.phone = "Null"
            if order.firstName == None:
                order.firstName = "Null"
            if order.lastName == None:
                order.lastName = "Null"


            orderList.append(order)
        return orderList
    except Exception as e:
        #logger.error(f"error occurred error -> {e} , userId -> {session['userId']}")
        return False

def getOrderOnDb(orderId):
    try:
        order = OrderTable.query.filter_by(orderId=orderId).one_or_none()
        return order
    except Exception as e:
        print(e)
        return False
