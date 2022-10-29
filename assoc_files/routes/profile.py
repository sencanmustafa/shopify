from flask import render_template,request , redirect,url_for
from assoc_files.utilities.utilities import login_required
from assoc_files.utilities.order import *
from assoc_files.database.modal import YurticiKargoApiInfo





@app.route('/updateprofile',methods=['POST'])
def updateProfile():
    if request.method == 'POST':
        try:
            companyName = request.form['companyName']
            email = request.form['email']
            phone = request.form['telefon']
            note = request.form['note']
            shopAdress = request.form['shopAdress']
            usernameGO = request.form['usernameGO']
            passwordGO = request.form['passwordGO']
            usernameKO = request.form['usernameKO']
            passwordKO = request.form['passwordKO']
            exist_dbuser = YurticiKargoApiInfo.query.filter_by(userId=session["userId"]).one_or_none()
            exist_dbuser.companyName = companyName
            exist_dbuser.domain = session["shop_url"]
            exist_dbuser.email = email
            exist_dbuser.phone = phone
            exist_dbuser.shop_address = shopAdress
            exist_dbuser.note = note
            exist_dbuser.userNameForGO = usernameGO
            exist_dbuser.userPasswordForGO = passwordGO
            exist_dbuser.userNameForKO = usernameKO
            exist_dbuser.userPasswordForKO = passwordKO

            YurticiKargoApiInfo.updateTable(exist_dbuser)
            return redirect(url_for("profile"))
        except Exception as e:
            print(e)
            flash("HATALI ISLEM","danger")
            return redirect(url_for("profile"))





@app.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    if request.method == 'POST':
        if  request.form['check']:
            print("check")
    if request.method == 'POST':
        try:
            companyName = request.form['companyName']
            email = request.form['email']
            phone = request.form['telefon']
            note = request.form['note']
            shopAdress = request.form['shopAdress']
            usernameGO = request.form['usernameGO']
            passwordGO = request.form['passwordGO']
            usernameKO = request.form['usernameKO']
            passwordKO = request.form['passwordKO']

            dbuser = YurticiKargoApiInfo(userId=session["userId"],domain=session["shop_url"],companyName=companyName,email=email,phone=phone,shop_address=shopAdress,note=note,userNameForGO=usernameGO,userPasswordForGO=passwordGO,userNameForKO=usernameKO,userPasswordForKO=passwordKO)
            YurticiKargoApiInfo.insert(dbuser)
            return redirect(url_for("profile"))
        except Exception as e:
            print(e)
            flash("HATALI ISLEM","danger")
            return redirect(url_for("profile"))
    try:
        existUser = YurticiKargoApiInfo.query.filter_by(userId=session["userId"]).one_or_none()
        if existUser !=None:
            return render_template("profile.html",existUser=existUser)
    except Exception as e:
        print(e)
        return render_template("profile.html")

