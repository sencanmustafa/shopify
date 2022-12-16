from assoc_files import app
from flask import session
from assoc_files.utilities.order import checkSessionUrl
from assoc_files.yurticiApi.cargoApi import *
from assoc_files.entity.UserClass import ShopInformation
from sqlalchemy.exc import SQLAlchemyError


def shopInfoAddDb(shop:ShopInformation):
    try:
        db_user = ShopInformationTable(shopId=shop.shopId,userId=shop.userId,email=shop.email,domain=shop.domain,address=shop.address,city=shop.city,phone=shop.phone,createdAt=shop.createdAt,customer_email=shop.customer_email,shop_owner=shop.shop_owner,primary_location_id=shop.primary_location_id)
        ShopInformationTable.insert(db_user)
        return True
    except SQLAlchemyError as e:
        print(e)
        return False

def jsonToShopInfo(data: dict):
    try:
        shop = ShopInformation()
        shop.shopId = data["shop"]["id"]
        shop.userId = session["userId"]
        shop.email = data["shop"]["email"]
        shop.domain = data["shop"]["domain"]
        shop.address = data["shop"]["address1"]
        shop.city = data["shop"]["city"]
        shop.phone = data["shop"]["phone"]
        shop.createdAt = data["shop"]["created_at"]
        shop.customer_email = data["shop"]["customer_email"]
        shop.shop_owner = data["shop"]["shop_owner"]
        shop.primary_location_id = data["shop"]["primary_location_id"]

        return shop
    except Exception as e:
        print(e)
        return False


def callShopInfo():
    checkSessionUrl()
    headers = {f"X-Shopify-Access-Token":session["accessToken"]}
    response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/shop.json",headers=headers)
    if response.status_code == 200:
        response = response.json()
        data = jsonToShopInfo(data=response)
        return data
    return False


def shopInfo():
    try:
        shop = callShopInfo()
        if shop:
            if shopInfoAddDb(shop=shop):
                return True
        return False
    except Exception as e:
        print(e)
        return False
