from assoc_files import app
import shopify
import binascii
import os

if __name__ == '__main__':

    app.run(debug=True,use_reloader=True,port=8080)