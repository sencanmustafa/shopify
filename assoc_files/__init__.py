from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__,static_folder="static")

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://shpadmin:Arm0@n!k32021@host.pl.armonikadijital.com.tr/ShopifyApp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usrshp61022_usr06102022:Arm@n!k32021@185.73.202.133/usrshp61022_db6102022'

db = SQLAlchemy(app)

app.config["API_KEY"] = "01f1fb02c1c85413aece6af94c8ec9e8"
app.config["SECRET_KEY"] = "f20bb93cbfa66d11cec02313e78e6fa9"
app.config["shop_url"] = ""
app.config["redirect_uri"] = "https://4dc0-188-132-132-178.ngrok.io/api"
app.config["api_version"]= "2022-07"
app.config["return_url"] = 'https://01b2-95-10-207-48.eu.ngrok.io/returnpayment'
app.config["access_scope_url"] = "https://armonika.myshopify.com/admin/oauth/access_scopes.json"



from assoc_files.routes import login
from assoc_files.routes import api
from assoc_files.routes import order
from assoc_files.routes import profile
from assoc_files.routes import payment



#from assoc_files.yurticiApi.checkTrackNumber import checkTrackNumber
#checkTrackNumber()
