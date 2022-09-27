import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["API_KEY"] = "01f1fb02c1c85413aece6af94c8ec9e8"
app.config["SECRET_KEY"] = "f20bb93cbfa66d11cec02313e78e6fa9"
app.config["shop_url"] = "https://armonika.myshopify.com/"
app.config["api_version"]= "2022-07"
app.config["redirect_uri"] = "https://7445-95-10-202-0.eu.ngrok.io/api"
app.config["access_token_url"] = f"{app.config['shop_url']}admin/oauth/access_token"

from assoc_files import routes
