from assoc_files import app
from assoc_files.entity.UserClass import User


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True,port=8080)
