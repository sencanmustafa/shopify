from assoc_files import db

class UserTable(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    shopurl = db.Column(db.String(225),unique=True,nullable=False)
    email = db.Column(db.String(100),nullable=True)
    password = db.Column(db.String(100),nullable=True)
    accessToken = db.Column(db.String(225),nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def updateTable(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return f" user -> {self.shopurl} - {self.accessToken}"

query = UserTable.query.all()
print(query)


class OrderTable(db.Model):
    __tablename__ = 'order'
    orderId = db.Column(db.Float, primary_key=True,nullable=False,unique=True)
    userId = db.Column(db.Integer,nullable=False)
    orderDate = db.Column(db.DateTime, nullable=False)
    firstName = db.Column(db.String(300),nullable=False)
    orderName = db.Column(db.String(300),nullable=False)
    orderStatus2 = db.Column(db.String(300),nullable=True)
    orderStatus = db.Column(db.Integer, nullable=True)
    lastName = db.Column(db.String(300),nullable=False)
    address1 = db.Column(db.String(300),nullable=False)
    phone = db.Column(db.String(300),nullable=False)
    city = db.Column(db.String(300),nullable=False)
    zip = db.Column(db.String(300),nullable=False)
    country = db.Column(db.String(300),nullable=False)
    address2 = db.Column(db.String(300),nullable=True)
    company = db.Column(db.String(300),nullable=False)
    name = db.Column(db.String(300),nullable=False)
    countryCode = db.Column(db.String(300),nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def updateTable(self):
        db.session.commit()
    def deleteOrder(self):
        db.session.delete(self)
        db.session.commit()

class YurticiKargoApiInfo(db.Model):
    __tablename__ = 'yurtici_kargo_api_info'
    shopPrimaryId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain = db.Column(db.String(300),nullable=False)
    companyName = db.Column(db.String(300),nullable=False)
    email = db.Column(db.String(300),nullable=False)
    phone  = db.Column(db.String(300),nullable=False)
    shop_address = db.Column(db.String(300),nullable=False)
    note = db.Column(db.String(300),nullable=False)
    userNameForGO = db.Column(db.String(300),nullable=False)
    userPasswordForGO = db.Column(db.String(300),nullable=False)
    userNameForKO = db.Column(db.String(300),nullable=False)
    userPasswordForKO = db.Column(db.String(300),nullable=False)
    userId = db.Column(db.Integer,nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
    def updateTable(self):
        db.session.commit()
    def deleteOrder(self):
        db.session.delete(self)
        db.session.commit()
