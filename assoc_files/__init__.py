import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["API_KEY"] = "26ff81e5c863fd7bf181e2e30eb40a06"
app.config["SECRET_KEY"] = "e4a7e6e2fb92df2f63d5904de42a0fee"
app.config["shop_url"] = "https://mustafa-flask.myshopify.com/"
app.config["api_version"]= "2022-07"
app.config["redirect_uri"] = "https://ec5a-95-10-206-177.eu.ngrok.io/api"
app.config["access_token_url"] = "https://mustafa-flask.myshopify.com/admin/oauth/access_token"
from assoc_files import routes
