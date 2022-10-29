from flask import render_template,request , redirect,url_for

from assoc_files.utilities.utilities import verifyLogin,validate ,deleteAccessToken
from assoc_files.utilities.order import *
#from assoc_files.log.logging import logger
from assoc_files.entity.UserClass import User
from assoc_files.yurticiApi.checkTrackNumber import checkTrackNumber
global user
global db_user
user = User()

@app.route('/',methods=['GET'])
def starter():
    return redirect(url_for("login"))


@app.route('/login',methods=['GET','POST'])
def login():
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



@app.route('/shopifylogin')
def shopifylogin():
    app.config["shop_url"] = request.args["shop"]
    print(user)
    dbUser = UserTable.query.filter_by(shopurl=app.config["shop_url"]).one_or_none()
    if verifyLogin(dbUser=dbUser) == True:
        user.shopUrl = dbUser.shopurl
        return redirect(url_for("info"))

    return redirect(url_for("goApi"))




@app.route('/disconnect',methods=['GET','POST'])
def disconnect():
    print(session.keys())
    print('*', session.values())
    deleteAccessToken()
    session.pop('accessToken',default='')
    return redirect(url_for("info"))


@app.route('/logout')
def logout():
    #logger.info(f"userId -> {session['userId']} logout")
    session.clear()
    return redirect(url_for("login"))
