from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import redis


app = Flask(__name__,static_folder="static")
app.secret_key = "super secret key"


load_dotenv()

API_KEY =os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
REDIRECT_URI=os.getenv("REDIRECT_URI")
API_VERSION=os.getenv("API_VERSION")
RETURN_URL=os.getenv("RETURN_URL")
ACCESS_SCOPE_URL =os.getenv("ACCESS_SCOPE_URL")
SHOP_URL = os.getenv("SHOP_URL")



app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
db = SQLAlchemy(app)





#rd = redis.Redis()


app.config["API_KEY"] = API_KEY
app.config["SECRET_KEY"] = SECRET_KEY
app.config["shop_url"] = ""
app.config["redirect_uri"] = REDIRECT_URI
app.config["api_version"]= API_VERSION
app.config["return_url"] = RETURN_URL
app.config["access_scope_url"] = ACCESS_SCOPE_URL



#app.config["SESSION_TYPE"] = "redis"
#app.config["SESSION_PERMANENT"] = True
#app.config["SESSION_USE_SIGNER"] = False
#App.config["SESSION_REDIS"] = rd.from_url("redis://127.0.0.1:6379")



#sess = Session(app)
#sess.init_app(app)



from assoc_files.routes import login
from assoc_files.routes import api
from assoc_files.routes import order
from assoc_files.routes import profile
from assoc_files.routes import payment
from assoc_files.routes import mandatoryWebhooks


#from assoc_files.yurticiApi.checkTrackNumber import checkTrackNumber
#checkTrackNumber()
