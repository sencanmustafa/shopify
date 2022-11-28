import time
from flask import render_template, request , redirect , url_for
from assoc_files.utilities.utilities import login_required, checkOrders
from assoc_files.utilities.order import *
#from assoc_files.log.logging import logger

from assoc_files.yurticiApi.checkTrackNumber import checkTrackNumber






@app.route('/updateorder/<int:orderId>',methods=['POST'])
@login_required
def updateOrder(orderId):
    try:
        if request.method !='POST':
            return redirect(url_for("login"))
        address = request.form['addressInput']
        if sendTagUpdateOrderAddress(orderId=orderId,address=address)==False:
            flash(message="Adres guncellenirken hata olustu", category="danger")
            return redirect(url_for("order"))
        flash(message="Adres basariyla guncellendi", category="success")
        return redirect(url_for("order"))
    except Exception as e:
        print(e)
        return redirect(url_for("login"))


@app.route('/printqr/<int:orderId>',methods=['POST'])
@login_required
def sendTagQr(orderId):
    try:

        if request.method !='POST':
            return redirect(url_for("login"))
        if sendTagPrintQr(orderId=orderId) == False:
            flash(message="Beklenmeyen bir hata olustu", category="danger")
            return redirect(url_for("order"))
        flash(message="Kargoya iletildi", category="danger")
        return redirect(url_for("order"))
    except Exception as e:
        print(e)
        return redirect(url_for("login"))

@app.route('/sendcargo/<int:orderId>',methods=['POST'])
@login_required
def sendCargo(orderId):
    try:
        if request.method !='POST':
            return redirect(url_for("login"))
        if sendTagCargo(orderId=orderId) == False:
            flash(message="Beklenmeyen bir hata olustu", category="danger")
            return redirect(url_for("order"))
        flash(message="Kargoya Veri Gonderildi", category="success")
        return redirect(url_for("orderBarkod"))
    except Exception as e:
        print(e)
        return redirect(url_for("login"))



@app.route('/order',methods=['GET'])
@login_required
def order():
    try:
        if request.method != 'GET':
            return redirect(url_for("login"))
        #logger.info(f"userId -> {session['userId']} called order function")
        orderData = callNewOrder()
        orderList = jsonToOrder(data=orderData)
        writeBarcode(orderList=orderList)
        checkOrderList = jsonToOrder(data=orderData)
        comparedOrderList = checkOrders(orderList=checkOrderList)
        insertOrderOnDb(comparedOrderList)
        return render_template("order.html",orders=orderList)
    except Exception as e:
        print(e)
        #logger.error(f"Error occurred {e} , userId -> {session['userId']}")
        return redirect(url_for("login"))


@app.route('/orderbarkod',methods=['GET'])
@login_required
def orderBarkod():
    try:
        if request.method != 'GET':
            return redirect(url_for("login"))
        orderData = callQrOrder()
        orderList = jsonToOrder(data=orderData)
        print(orderList,"orderlist")
        return render_template("barkod.html",orders=orderList)
    except Exception as e:
        print(e)
        return redirect(url_for("info"))

@app.route('/ordercargo',methods=['GET'])
@login_required
def orderCargo():
    try:
        if request.method != 'GET':
            return redirect(url_for("login"))
        #checkTrackNumber()
        time.sleep(3)
        orderData = callCargoOrder()
        orderList = jsonToOrder(data=orderData)
        print(orderList, "orderlist")
        return render_template("takip_bekleyenler.html", orders=orderList)
    except Exception as e:
        print(e)
        return redirect(url_for("info"))


@app.route('/shipping',methods=['GET'])
@login_required
def shipping():
    try:
        if request.method != 'GET':
            return redirect(url_for("login"))
        fulFillment()
        #orderData = callShippingOrder()
        #orderList = jsonToOrder(data=orderData)
        orderList = OrderTable.query.filter_by(userId=session["userId"],orderStatus=4).all()
        return render_template("dagitim.html",orders=orderList)
    except Exception as e:
        print(e)
        return redirect(url_for("info"))


@app.route('/info')
@login_required
def info():
    print('*',session.values())
    print(session.keys())

    return render_template("info.html")

