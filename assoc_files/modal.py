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

    def updateUserTable(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return f" user -> {self.email} - {self.accessToken}"
