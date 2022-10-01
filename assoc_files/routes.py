import binascii
import os
import requests
import shopify
from flask import render_template, redirect, url_for, request, session
from assoc_files.entity.UserClass import User ,Order
from assoc_files.modal import UserTable
from assoc_files import app
from assoc_files.utilities.utilities import login_required,jsonToObject,validate , UpdatetUserOnDb,insertOrderOnDb, token_required , getOrder,jsonify
from assoc_files.log.logging import *

from assoc_files.data import data



#shopify.Session.setup(api_key=app.config['API_KEY'], secret=app.config['SECRET_KEY'])
#client = shopify.Session(app.config['shop_url'], app.config['api_version'])
#scope = ["read_products", "write_products"]

shop_url = app.config['shop_url']
api_version = '2020-07'
state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
redirect_uri = app.config["redirect_uri"]
scopes = ['read_products', 'read_orders']


shopify.Session.setup(api_key=app.config["API_KEY"],secret=app.config["SECRET_KEY"])
newSession = shopify.Session(app.config['shop_url'], app.config["api_version"])
auth_url = newSession.create_permission_url(scopes, redirect_uri, state)




@app.route('/go_api')
def goApi():
    logger.info(f"userId -> {session['userId']} called goApi function")
    return redirect(auth_url)

@app.route('/logout')
def logout():
    logger.info(f"userId -> {session['userId']} logout")
    session.clear()
    return redirect(url_for("login"))

@app.route('/',methods=['GET'])
def starter():
    return redirect(url_for("login"))

@app.route('/login',methods=['GET','POST'])
def login():
    global user
    global db_user
    if request.method == 'POST':
        db_user = UserTable.query.filter_by(email=request.form['email']).one_or_none()
        print(db_user)
        user = User(email=request.form['email'],password=request.form['password'])
        if validate(user=user,dbUser=db_user) == True:
            print(session["accessToken"])
            logger.info(f"userId -> {session['userId']} logged in")
            return redirect(url_for("info"))

    return render_template("index.html")



@app.route('/info')
@login_required
def info():
    return render_template("info.html")

@app.route('/api')
def api():
    try:
        logger.info(f" userId -> {session['userId']} called api function")
        code = request.args['code']
        shop = request.args['shop']
        timestamp =request.args["timestamp"]

        params = dict({"client_id":app.config["API_KEY"],"client_secret":app.config["SECRET_KEY"],"code":code,"shop":shop,"timestamp":timestamp})

        response = requests.post(app.config["access_token_url"],data=params)

        session["accessToken"] = response.json()['access_token']

        user.accessToken = session["accessToken"]

        UpdatetUserOnDb(user=user)
        return redirect(url_for("info"))
    except Exception as e:
        logger.error(f"error occurred in api function error -> {e} , userId -> {session['userId']}")
        return redirect(url_for("info"))



@app.route('/success')
def success():
    sesion = shopify.Session(app.config['shop_url'], app.config["api_version"], session["access_token"])
    shopify.ShopifyResource.activate_session(sesion)

    return f"your logged succes "

@app.route('/order',methods=['GET','POST'])
def order():
    try:
        logger.info(f"userId -> {session['userId']} called order function")
        #orderData = getOrder(app.config["order_url"])
        orderData = data["shipping_address"]
        print(orderData)
        order = Order()
        order = jsonToObject(data=orderData,order=order)
        insertOrderOnDb(order)
        return 'success'
    except Exception as e:
        logger.error(f"Error occurred {e} , userId -> {session['userId']}")
        return redirect(url_for("info"))










