from flask_sqlalchemy import SQLAlchemy
from assoc_files import db
import pandas as pd
from assoc_files import app

class UserTable(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    accessToken = db.Column(db.String(225))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def updateTable(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return f" user -> {self.email} - {self.accessToken}"

class OrderTable(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer,nullable=False)
    orderDate = db.Column(db.DateTime, nullable=False)
    firstName = db.Column(db.String(45),nullable=False)
    lastName = db.Column(db.String(45),nullable=False)
    address1 = db.Column(db.String(300),nullable=False)
    phone = db.Column(db.String(45),nullable=False)
    city = db.Column(db.String(45),nullable=False)
    zip = db.Column(db.String(45),nullable=False)
    country = db.Column(db.String(45),nullable=False)
    address2 = db.Column(db.String(300),nullable=True)
    company = db.Column(db.String(45),nullable=False)
    name = db.Column(db.String(150),nullable=False)
    countryCode = db.Column(db.String(45),nullable=False)

    """
    def __str__(self):
        return f"order orderId -> {self.id},userId -> {self.userId}, firstName -> {self.firstName}, lastName -> {self.lastName},address -> {self.address1}, phone-> {self.phone},orderDate->{self.orderDate}"
    """
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def updateTable(self):
        db.session.commit()
    def deleteOrder(self):
        db.session.delete(self)
        db.session.commit()
