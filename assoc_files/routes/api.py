from flask import  request
from assoc_files.utilities.utilities import createAuthUrl
from assoc_files.utilities.order import *

from assoc_files.routes.login import user

@app.route('/api')
def api():
    try:
        print(session.keys())
        print('*', session.values())
        #logger.info(f" user -> {user.email} called api function")
        print(request.args)
        code = request.args['code']
        shop = request.args['shop']
        timestamp =request.args["timestamp"]
        params = dict({"client_id":app.config['API_KEY'],"client_secret":app.config["SECRET_KEY"],"code":code,"shop":shop,"timestamp":timestamp})
        access_token_url = f"https://{app.config['shop_url']}/admin/oauth/access_token"
        response = requests.post(access_token_url,data=params)
        session["accessToken"] = response.json()['access_token']
        user.accessToken = session["accessToken"]
        user.shopUrl = app.config['shop_url']

        #InsertUserOnDb(user=user)
        session["logged_in"] = True
        return redirect(url_for("info"))
    except Exception as e:
        #logger.error(f"error occurred in api function error -> {e} , user -> {user.email}")
        user.shopUrl = None
        print(e)
        return redirect(url_for("login"))

@app.route('/go_api')
def goApi():
    print(user)
    #logger.info(f"userId -> {session['userId']} called goApi function")

    try:
        requests.get(url=createAuthUrl())
        return redirect(createAuthUrl())
    except Exception as e:
        print(e)
        flash(message="lutfen dogru bir magaza adi girdiginizden emin olunuz",category="danger")
        return redirect(url_for("login"))


@app.route('/getToken',methods=['GET'])
def getToken():
    return 'Please Get Token'
