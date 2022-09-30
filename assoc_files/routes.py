import binascii
import os
import requests
import shopify
from functools import wraps
from flask import render_template, redirect, url_for, request, Response, session, jsonify
from html5lib import serialize
from assoc_files.entity.UserClass import User , validate , UpdatetUserOnDb
from assoc_files.modal import UserTable
from assoc_files import app
from assoc_files import db

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
        if "access_token" in session:
            return f(*args,**kwargs)
        else:
            return redirect(url_for("token_page"))
    return decorated_function

@app.route('/home')
def home():
    return redirect(auth_url)

@app.route('/logout')
def logout():
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
        db_user = UserTable.query.filter_by(email=request.form['email']).first()
        print(db_user)
        user = User(email=request.form['email'],password=request.form['password'])
        print(validate(user=user,dbUser=db_user) == True)
        if validate(user=user,dbUser=db_user) == True:
            return redirect(url_for("info"))




    return render_template("index.html")



@app.route('/info')
@login_required
def info():
    return render_template("info.html")







@app.route('/api')
def api():
    code = request.args['code']
    shop = request.args['shop']
    timestamp =request.args["timestamp"]

    params = dict({"client_id":app.config["API_KEY"],"client_secret":app.config["SECRET_KEY"],"code":code,"shop":shop,"timestamp":timestamp})

    response = requests.post(app.config["access_token_url"],data=params)

    session["accessToken"] = response.json()['access_token']

    user.accessToken = session["accessToken"]

    updateUser = UpdateUserOnDb(user=user)


    return f"{session['accessToken']}"

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






def serialize_model(model):
    return jsonify(serialize(model))








