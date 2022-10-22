import time

import barcode
from flask import render_template, request
from assoc_files.utilities.utilities import login_required
from assoc_files.utilities.order import *
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter
from barcode import generate
#from assoc_files.log.logging import logger


@app.route('/deneme',methods=['GET'])
def deneme():
    Code128 = barcode.get_barcode_class('code128')
    my_code = Code128("123456",writer=ImageWriter())
    fullName = my_code.save('code128_barcode')
    print(fullName)
    fp = BytesIO()

    #with open('assoc_files/routes','wb') as f:
    #    my_code.write(f)
    #generate('Code128','123456',writer=ImageWriter(),output=fp)
    return fullName


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
    if sendTagPrintQr(orderId=orderId) == False:
        flash(message="Beklenmeyen bir hata olustu", category="danger")
        return redirect(url_for("order"))
    flash(message="Kargoya iletildi", category="danger")
    return redirect(url_for("orderBarkod"))


@app.route('/sendcargo/<int:orderId>',methods=['POST'])
def sendCargo(orderId):
    if sendTagCargo(orderId=orderId) == False:
        flash(message="Adres guncellenirken hata olustu", category="danger")
        return redirect(url_for("order"))

    flash(message="Adres basariyla guncellendi", category="success")
    return redirect(url_for("orderCargo"))




@app.route('/order',methods=['GET'])
def order():
    try:
        #logger.info(f"userId -> {session['userId']} called order function")
        orderData = callNewOrder()
        orderList = jsonToOrder(data=orderData)
        #insertOrderOnDb(orderList)
        return render_template("order.html",orders=orderList)
    except Exception as e:
        print(e)
        #logger.error(f"Error occurred {e} , userId -> {session['userId']}")
        return redirect(url_for("login"))


@app.route('/orderbarkod',methods=['GET'])
def orderBarkod():
    try:
        time.sleep(3)
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
        return render_template("cargo.html", orders=orderList)
    except Exception as e:
        print(e)
        return redirect(url_for("info"))





@app.route('/info')
@login_required
def info():
    print('*',session.values())
    print(session.keys())

    return render_template("info.html")

