import binascii
import json
import os
import urllib.request
import hmac
import requests
import shopify
from flask import render_template, redirect, url_for, request, Response, session, jsonify
from html5lib import serialize

from assoc_files import app

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




@app.route('/home')
def home():
    return redirect(auth_url)


@app.route('/api')
def api():
    code = request.args['code']
    shop = request.args['shop']
    timestamp =request.args["timestamp"]

    params = dict({"client_id":app.config["API_KEY"],"client_secret":app.config["SECRET_KEY"],"code":code,"shop":shop,"timestamp":timestamp})

    response = requests.post(app.config["access_token_url"],data=params)

    session["access_token"] = response.json()['access_token']

    params = dict(
        {"client_id": app.config["API_KEY"], "client_secret": app.config["SECRET_KEY"], "code": code, "shop": shop,"timestamp": timestamp,"access_token":session['access_token']})



    return redirect(url_for("product"))




@app.route('/success')
def success():
    sesion = shopify.Session(app.config['shop_url'], app.config["api_version"], session["access_token"])
    shopify.ShopifyResource.activate_session(sesion)

    return f"your logged succes "

@app.route('/product')
def product():
    print(session['access_token'])
    header = {f"X-Shopify-Access-Token":session["access_token"]}
    #response2 = requests.get("https://armonika.myshopify.com/admin/api/2022-07/orders.json?status=any",headers=header)
    #print(response2)

    response = requests.get("https://armonika.myshopify.com/admin/api/2022-07/orders.json?status=any",headers=header)
    #response = requests.get("https://armonika.myshopify.com/admin/oauth/access_scopes.json", headers=header)
    data = response.json()
    return data
    #sesion = shopify.Session(app.config['shop_url'], app.config["api_version"], session["access_token"])
    #print(sesion)
    #shopify.ShopifyResource.activate_session(sesion)
    #shop = shopify.Shop.current()
    #orders = shopify.Order.find(status='any')
    #print(orders)
    #print(shop.name)
    #product = shopify.Product._find_every()
    #for i in product:
    #    print(i.title)
#
    #return 'mustafa'






def serialize_model(model):
    return jsonify(serialize(model))

#@app.route('/api',methods = ['GET','POST'])
#def route():
#    if request.args.get('shop'):
#        params = {"client_id":app.config["API_KEY"],"client_secret":app.config["SECRET_KEY"],"code":request.args.get("code"),"timestamp":request.args.get("timestamp")}
#        #"hmac": request.args.get("hmac"),
#        req = requests.post(f"https://mustafa-flask.myshopify.com/admin/oauth/access_token",data=params)
#
#
#
#
#        auth_client = shopify.Session(app.config['shop_url'],app.config['api_version'],app.config["access_token"])
#        shopify.ShopifyResource.activate_session(auth_client)
#        print(shopify.ShopifyResource.activate_session(auth_client))

#   return redirect(url_for("success"))




#@app.route('/home',methods = ['GET','POST'])
#def home_route():
#    auth_url = f"{app.config['shop_url']}admin/oauth/authorize?client_id={app.config['API_KEY']}&scope=read_products&redirect_uri={app.config['redirect_uri']}"
#    print("debug - auth Url" , auth_url)
#    return redirect(auth_url)







