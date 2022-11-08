from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os



app = Flask(__name__,static_folder="static")


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usrshp61022_usr06102022:Arm@n!k32021@185.73.202.133/usrshp61022_db6102022'

load_dotenv()

API_KEY =os.getenv("API_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
REDIRECT_URI=os.getenv("REDIRECT_URI")
API_VERSION=os.getenv("API_VERSION")
RETURN_URL=os.getenv("RETURN_URL")
ACCESS_SCOPE_URL =os.getenv("ACCESS_SCOPE_URL")
SHOP_URL = os.getenv("SHOP_URL")



app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

app.config["API_KEY"] = API_KEY
app.config["SECRET_KEY"] = SECRET_KEY
app.config["shop_url"] = ""
app.config["redirect_uri"] = REDIRECT_URI
app.config["api_version"]= API_VERSION
app.config["return_url"] = RETURN_URL
app.config["access_scope_url"] = ACCESS_SCOPE_URL



from assoc_files.routes import login
from assoc_files.routes import api
from assoc_files.routes import order
from assoc_files.routes import profile
from assoc_files.routes import payment



#from assoc_files.yurticiApi.checkTrackNumber import checkTrackNumber
#checkTrackNumber()
