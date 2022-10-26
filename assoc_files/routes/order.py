import time
from flask import render_template, request , redirect , url_for
from assoc_files.utilities.utilities import login_required, checkOrders,callYurticiUser
from assoc_files.utilities.order import *
#from assoc_files.log.logging import logger
from assoc_files.yurticiApi.cargoApi import *

@app.route('/updateorder/<int:orderId>',methods=['POST'])
def updateOrder(orderId):
    address = request.form['addressInput']
    if sendTagUpdateOrderAddress(orderId=orderId,address=address)==False:
        flash(message="Adres guncellenirken hata olustu", category="danger")
        return redirect(url_for("order"))
    flash(message="Adres basariyla guncellendi", category="success")
    return redirect(url_for("order"))

@app.route('/printqr/<int:orderId>',methods=['POST'])
def printqr(orderId):
    if writeBarcode(orderId=orderId) == False:
        flash(message="Beklenmeyen bir hata olustu", category="danger")
        return redirect(url_for("order"))
    if sendTagPrintQr(orderId=orderId) == False:
        flash(message="Beklenmeyen bir hata olustu", category="danger")
        return redirect(url_for("order"))
    flash(message="Kargoya iletildi", category="danger")
    return redirect(url_for("order"))


@app.route('/sendcargo/<int:orderId>',methods=['POST'])
def sendCargo(orderId):
    if sendTagCargo(orderId=orderId) == False:
        flash(message="Beklenmeyen bir hata olustu", category="danger")
        return redirect(url_for("order"))
    flash(message="Kargoya Veri Gonderildi", category="success")
    return redirect(url_for("orderBarkod"))




@app.route('/order',methods=['GET'])
def order():
    try:
        #logger.info(f"userId -> {session['userId']} called order function")
        orderData = callNewOrder()
        orderList = jsonToOrder(data=orderData)
        checkOrderList = jsonToOrder(data=orderData)
        comparedOrderList = checkOrders(orderList=checkOrderList)
        insertOrderOnDb(comparedOrderList)
        return render_template("order.html",orders=orderList)
    except Exception as e:
        print(e)
        #logger.error(f"Error occurred {e} , userId -> {session['userId']}")
        return redirect(url_for("login"))


@app.route('/orderbarkod',methods=['GET'])
def orderBarkod():
    try:
        orderData = callQrOrder()
        orderList = jsonToOrder(data=orderData)
        print(orderList,"orderlist")
        return render_template("barkod.html",orders=orderList)
    except Exception as e:
        print(e)
        return redirect(url_for("info"))

@app.route('/ordercargo',methods=['GET'])
def orderCargo():
    try:
        time.sleep(3)
        orderData = callCargoOrder()
        orderList = jsonToOrder(data=orderData)
        print(orderList, "orderlist")
        return render_template("takip_bekleyenler.html", orders=orderList)
    except Exception as e:
        print(e)
        return redirect(url_for("info"))


@app.route('/shipping',methods=['GET'])
def shipping():
    try:
        pass
    except Exception as e:
        print(e)
        return redirect(url_for("info"))


@app.route('/info')
@login_required
def info():
    print('*',session.values())
    print(session.keys())

    return render_template("info.html")

