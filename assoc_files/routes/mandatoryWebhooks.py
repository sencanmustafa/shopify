from flask import render_template,request , redirect,url_for,jsonify

from assoc_files.utilities.utilities import verifyLogin,validate ,deleteAccessToken
from assoc_files.utilities.order import *


@app.route('/customers/data_request')
def customerDataRequest():
    return 200


@app.route('/customers/redact')
def customerRedact():
    return 200

@app.route('/shop/redact')
def shopRedact():
    return 200