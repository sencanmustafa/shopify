from assoc_files import app
from threading import  Thread
from dotenv import load_dotenv
import os
from wsgiref.simple_server import make_server

API_KEY =os.getenv("API_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
REDIRECT_URI=os.getenv("REDIRECT_URI")
API_VERSION=os.getenv("API_VERSION")
RETURN_URL=os.getenv("RETURN_URL")
ACCESS_SCOPE_URL =os.getenv("ACCESS_SCOPE_URL")
SHOP_URL = os.getenv("SHOP_URL")


def run_app():
    app.run(debug=True,use_reloader=True,port=8080)



if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, use_reloader=True, port=8080)
    #thread = Thread(target=run_app)
    #thread.start()

