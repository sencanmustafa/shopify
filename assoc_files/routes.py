import binascii
import os
import requests

from flask import render_template, redirect, url_for, request, session
from assoc_files.entity.UserClass import User ,Order
from assoc_files.modal import UserTable
from assoc_files import app
from assoc_files.utilities.utilities import getOrderOnDb,login_required,jsonToOrder,verifyLogin,validate ,InsertUserOnDb,insertOrderOnDb,deleteAccessToken, token_required , getOrder,jsonify
#from assoc_files.log.logging import logger
from assoc_files.log.logging import *



#

state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
redirect_uri = app.config["redirect_uri"]
scopes = ['read_products', 'read_orders']
scopes_string = ','.join(scopes)

def createAuthUrl():
    auth_url = f"https://{app.config['shop_url']}/admin/oauth/authorize?client_id={app.config['API_KEY']}&scope={scopes_string}&redirect_uri={app.config['redirect_uri']}&state={state}"
    return auth_url

@app.route('/shopifylogin')
def shopifylogin():
    app.config["shop_url"] = request.args["shop"]
    dbUser = UserTable.query.filter_by(shopurl=app.config["shop_url"]).one_or_none()
    if verifyLogin(dbUser=dbUser) == True:
        return redirect(url_for("goApi"))

    return app.config["shop_url"]



@app.route('/login',methods=['GET','POST'])
def login():
    global user
    user = User()
    global db_user

    if request.method == 'POST':
        if request.form['storeName']:
            #db_user = UserTable.query.filter_by(shopurl=request.form['storeName']).one_or_none()
            #armonika.myshopify.com
            app.config["shop_url"] = request.form['storeName']
            user.shopUrl = app.config["shop_url"]
            return redirect(url_for("goApi"))
        else:
            db_user = UserTable.query.filter_by(email=request.form['email']).one_or_none()
            user.email=request.form['email']
            user.password = request.form['password']
            if validate(user=user,dbUser=db_user) == True:
                print(session["accessToken"])
                #logger.info(f"userId -> {session['userId']} logged in")
                return redirect(url_for("info"))

    return render_template("index.html")

@app.route('/go_api')
def goApi():
    #logger.info(f"userId -> {session['userId']} called goApi function")
    print(createAuthUrl())
    return redirect(createAuthUrl())


@app.route('/api')
def api():
    try:
        print('*', session.values())
        print(session.keys())
        #logger.info(f" user -> {user.email} called api function")
        print(request.args)
        code = request.args['code']
        shop = request.args['shop']
        timestamp =request.args["timestamp"]
        params = dict({"client_id":app.config["API_KEY"],"client_secret":app.config["SECRET_KEY"],"code":code,"shop":shop,"timestamp":timestamp})
        access_token_url = f"https://{app.config['shop_url']}/admin/oauth/access_token"
        response = requests.post(access_token_url,data=params)
        session["accessToken"] = response.json()['access_token']
        user.accessToken = session["accessToken"]
        InsertUserOnDb(user=user)
        session["logged_in"] = True
        return redirect(url_for("info"))
    except Exception as e:
        #logger.error(f"error occurred in api function error -> {e} , user -> {user.email}")
        user.shopUrl = None
        print(e)
        return redirect(url_for("info"))


@app.route('/order',methods=['GET','POST'])
def order():
    try:
        #logger.info(f"userId -> {session['userId']} called order function")
        orderData = getOrder()

        orderList = jsonToOrder(data=orderData)

        #insertOrderOnDb(order)

        return render_template("order.html",orders=orderList)
    except Exception as e:
        #logger.error(f"Error occurred {e} , userId -> {session['userId']}")
        return redirect(url_for("info"))


@app.route('/vieworders',methods=['GET','POST'])
@login_required
def viewOrder():
    orders = getOrderOnDb()
    return render_template("order.html",orders=orders)

@app.route('/',methods=['GET'])
def starter():
    return redirect(url_for("login"))

@app.route('/getToken',methods=['GET'])
def getToken():
    return 'Please Get Token'

@app.route('/info')
@login_required
def info():
    print('*',session.values())
    print(session.keys())

    return render_template("info.html")


@app.route('/disconnect',methods=['GET','POST'])
def disconnect():
    deleteAccessToken()
    session.pop('accessToken',default='')
    return redirect(url_for("info"))


#@app.route('/success',methods=['GET'])
#def success():
#    sesion = shopify.Session(app.config['shop_url'], app.config["api_version"], session["access_token"])
#    shopify.ShopifyResource.activate_session(sesion)
#
#    return f"your logged succes "

@app.route('/logout')
def logout():
    #logger.info(f"userId -> {session['userId']} logout")
    session.clear()
    return redirect(url_for("login"))
"""
https://apps.armonikadijital.com/tolga/login?hmac=9ca1a762cc19305142d4b9268a60cbc25dfef42f29386111b362bfb974773077&
host=YXJtb25pa2EubXlzaG9waWZ5LmNvbS9hZG1pbg&
session=2ca8e76eefdc12dd9b34bf919ac1ee115229c346fcc84533a53b4c3db853a0b2&\
         shop=armonika.myshopify.com&timestamp=1665676159
"""
