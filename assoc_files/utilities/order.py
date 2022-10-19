import requests
from assoc_files import app
from flask import session, redirect, url_for


def getNewOrder():
    if app.config["shop_url"] == '' or app.config["shop_url"] == None:
        return redirect(url_for("login"))
    header = {f"X-Shopify-Access-Token": session["accessToken"],"Content-Type": "application/json" }
    response = requests.get(f"https://{app.config['shop_url']}/admin/api/2022-07/orders.json?financial_status:paid AND fulfillment_status:unshipped",headers=header)
    data = response.json()

    return data


def updateShopifyOrder(orderId,address):
    if app.config["shop_url"] == '' or app.config["shop_url"] == None:
        return redirect(url_for("login"))
    headers = {f"X-Shopify-Access-Token":session["accessToken"]}

    json_data = {
        'order': {
            'id': orderId,
            'tags':'Adres Duzenlendi',
            'shipping_address': {
                'address1': address
            },
        },
    }

    response = requests.put(f"https://{app.config['shop_url']}/admin/api/2022-07/orders/{orderId}.json",headers=headers, json=json_data)
    return True
