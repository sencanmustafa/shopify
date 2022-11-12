from assoc_files import app


from dotenv import load_dotenv
import os


API_KEY =os.getenv("API_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
REDIRECT_URI=os.getenv("REDIRECT_URI")
API_VERSION=os.getenv("API_VERSION")
RETURN_URL=os.getenv("RETURN_URL")
ACCESS_SCOPE_URL =os.getenv("ACCESS_SCOPE_URL")
SHOP_URL = os.getenv("SHOP_URL")

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True,use_reloader=True,port=8080)

