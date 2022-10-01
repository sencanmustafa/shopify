from assoc_files.modal import UserTable,OrderTable
from flask import session
import datetime
class User:
    def __init__(self,email=None,password=None,accessToken=None):
        self.email = email
        self.password = password
        self.accessToken = accessToken
    def __str__(self):
        return f"{self.email} , {self.accessToken}"
class Order:
    def __init__(self,firstName=None,lastName=None,address1=None,phone=None,city=None,zip=None,country=None,address2=None,company=None,name=None,countryCode=None):
        self.firstName=firstName
        self.lastName=lastName
        self.address1=address1
        self.phone=phone
        self.city=city
        self.zip=zip
        self.country=country
        self.address2=address2
        self.company=company
        self.name=name
        self.countryCode=countryCode


