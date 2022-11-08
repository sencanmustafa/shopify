from assoc_files import app
from flask import session, redirect, url_for, request, flash
import requests
from assoc_files.database.modal import UserTable,ShopInformationTable
from assoc_files.utilities.shopInfo import shopInfo
from assoc_files.utilities.order import fulFillment
from dotenv import load_dotenv
import os
load_dotenv()

RETURN_URL=os.getenv("RETURN_URL")




@app.route('/basicpayment',methods=['GET'])
def basicPayment():
    try:
        header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
        json_data = {'recurring_application_charge': {'name': 'Armonika Basic Plan','trial_days':1,'price': 0.1,'test':True,'return_url':RETURN_URL,},}
        response = requests.post(f'https://{app.config["shop_url"]}/admin/api/2022-07/recurring_application_charges.json',headers=header, json=json_data)
        if response.status_code == 201:
            response = response.json()
            return redirect(response["recurring_application_charge"]["confirmation_url"])
    except Exception as e:
        print(e)
        flash("error occurred please contact armonika","danger")
        return redirect(url_for("login"))

@app.route('/returnpayment',methods=['GET','POST'])
def returnPayment():
    chargeId = request.args['charge_id']

    return redirect(url_for("checkCharge",chargeid=chargeId))


@app.route('/checkusercharge',methods=['GET','POST'])
def checkUserCharge():
    try:
        db_user = UserTable.query.filter_by(id=session["userId"]).one_or_none()
        if db_user!=None:
            chargeid = db_user.chargeId
            if chargeid !=None:
                return redirect(url_for("checkCharge",chargeid=chargeid))
            else:
                return redirect(url_for("basicPayment"))
    except Exception as e:
        print(e)
        flash("error occurred please contact armonika", "danger")
        return redirect(url_for("login"))

@app.route('/checkcharge/<int:chargeid>',methods=['GET','POST'])
def checkCharge(chargeid):
    try:
        if chargeid != None:
            header = {f"X-Shopify-Access-Token": session["accessToken"], "Content-Type": "application/json"}
            response = requests.get(f'https://{app.config["shop_url"]}/admin/api/2022-07/recurring_application_charges/{chargeid}.json', headers=header)
            response = response.json()
            if response["recurring_application_charge"]["status"] == "active":
                try:
                    db_user = UserTable.query.filter_by(id=session["userId"]).one_or_none()
                    db_user2 = ShopInformationTable.query.filter_by(userId=session["userId"]).one_or_none()
                    if db_user!=None:
                        db_user.chargeId = chargeid
                        db_user.chargeStartDate = response["recurring_application_charge"]["created_at"]
                        UserTable.updateTable(db_user)
                        ## GET SHOP INFORMATION FUNCTION ##
                        shopInfo(user=db_user2)
                        ## GET SHOP INFORMATION FUNCTION ##


                        return redirect(url_for("info"))
                except Exception as e:
                    print(e)
                    return redirect(url_for("login"))
            else:
                return redirect(url_for("basicPayment"))
        else:
            return redirect(url_for("basicPayment"))
    except Exception as e:
        print(e)
        flash("error occurred please contact armonika","danger")
        return redirect(url_for("login"))




