class User:
    def __init__(self,email=None,password=None,accessToken=None,shopUrl=None):
        self.email = email
        self.password = password
        self.accessToken = accessToken
        self.shopUrl=shopUrl
    def __str__(self):
        return f"{self.shopUrl} , {self.accessToken}"
class Order:
    def __init__(self,orderId=None,firstName=None,lastName=None,orderName=None,fulfillment_status=None,orderStatus=None,date=None,address1=None,phone=None,orderStatusStr=None,city=None,zip=None,country=None,address2=None,tag=None,company=None,name=None,countryCode=None):
        self.orderId = orderId
        self.firstName=firstName
        self.lastName=lastName
        self.orderStatus=orderStatus
        self.orderStatusStr = orderStatusStr
        self.fulfillment_status = fulfillment_status
        self.orderName=orderName
        self.date = date
        self.address1=address1
        self.phone=phone
        self.city=city
        self.zip=zip
        self.country=country
        self.address2=address2
        self.company=company
        self.name=name
        self.countryCode=countryCode
        self.tag = tag



