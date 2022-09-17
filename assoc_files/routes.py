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
shopify.Session.setup(api_key=app.config['API_KEY'], secret=app.config['SECRET_KEY'])
client = shopify.Session(app.config['shop_url'], app.config['api_version'])
state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
scope = ["read_products", "write_products"]

def serialize_model(model):
    return jsonify(serialize(model))

@app.route('/api',methods = ['GET','POST'])
def route():
    if request.args.get('shop'):
        params = {"client_id":app.config["API_KEY"],"client_secret":app.config["SECRET_KEY"],"code":request.args.get("code"),"timestamp":request.args.get("timestamp")}
        #"hmac": request.args.get("hmac"),
        req = requests.post(f"https://mustafa-flask.myshopify.com/admin/oauth/access_token",data=params)




        auth_client = shopify.Session(app.config['shop_url'],app.config['api_version'],app.config["access_token"])
        shopify.ShopifyResource.activate_session(auth_client)

        print(shopify.Shop.current())
        a = shopify.Product.find()
        print(a[0].title)
    return "Mustafa"




@app.route('/home',methods = ['GET','POST'])
def home_route():
    auth_url = f"{app.config['shop_url']}admin/oauth/authorize?client_id={app.config['API_KEY']}&scope=read_products&redirect_uri={app.config['redirect_uri']}"
    print("debug - auth Url" , auth_url)
    return redirect(auth_url)







