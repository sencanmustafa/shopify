import requests , xmltodict
from assoc_files.database.modal import *
from assoc_files.entity.UserClass import *
from random import randint



cargoUrl="http://testwebservices.yurticikargo.com:9090/KOPSWebServices/ShippingOrderDispatcherServices?wsdl "
cargoHeaders = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}
f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices"> 

   <soapenv:Header/> 

   <soapenv:Body> 

      <ship:queryShipment> 

         <wsUserName>YKTEST</wsUserName><wsPassword>YK</wsPassword><wsLanguage>TR</wsLanguage> 

        <keys>45251841875415899</keys> 

         <keyType>0</keyType> 

         <addHistoricalData>false</addHistoricalData> 

         <onlyTracking>false</onlyTracking> 

      </ship:queryShipment > 

   </soapenv:Body> 

</soapenv:Envelope> """


"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices">

       <soapenv:Header/>

       <soapenv:Body>

          <ship:createShipment>

             <wsUserName>YKTEST</wsUserName><wsPassword>YK</wsPassword><userLanguage>TR</userLanguage>

          <ShippingOrderVO><cargoKey>4525184187541589</cargoKey><invoiceKey>4525184187541589</invoiceKey><receiverCustName>ALICI ADI</receiverCustName><receiverAddress>ALICI SEVK ADRESi Kargo Plaza K:5 Maslak</receiverAddress><cityName>istanbul</cityName><townName>sisli</townName><receiverPhone1>2123652365</receiverPhone1><taxOfficeId/><cargoCount>1</cargoCount><specialField1>1$1340965#</specialField1><ttDocumentId/><dcSelectedCredit/><dcCreditRule/><orgReceiverCustId>11988</orgReceiverCustId></ShippingOrderVO></ship:createShipment>

       </soapenv:Body>

    </soapenv:Envelope>
"""

#response = requests.post(url=cargoUrl,data=createShipmentBody,headers=cargoHeaders)
#obj = xmltodict.parse(response.content)
#
#print(obj)



def createShipment(userYurtici:ShopInformationTable,order:Order):
    createShipmentBody = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices">
       <soapenv:Header/>
       <soapenv:Body>
          <ship:createShipment>
             <wsUserName>{userYurtici.userNameForGO}</wsUserName><wsPassword>{userYurtici.userPasswordForGO}</wsPassword><userLanguage>TR</userLanguage>
          <ShippingOrderVO><cargoKey>{order.orderId}</cargoKey><invoiceKey>{order.orderId}</invoiceKey><receiverCustName>{order.name}</receiverCustName><receiverAddress>{order.address1}</receiverAddress><cityName>{order.address2}</cityName><receiverPhone1>{order.phone}</receiverPhone1></ShippingOrderVO></ship:createShipment>
       </soapenv:Body>
    </soapenv:Envelope>"""

    response = requests.post(url=cargoUrl,data=createShipmentBody,headers=cargoHeaders)
    if response.status_code == 200:

        obj = xmltodict.parse(response.content)
        print(obj)
        return True
    return False


def queryShipment(orderId):
    queryShipmentBody = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices"> 
       <soapenv:Header/> 
       <soapenv:Body> 
          <ship:queryShipment> 
             <wsUserName>YKTEST</wsUserName><wsPassword>YK</wsPassword><wsLanguage>TR</wsLanguage> 
            <keys>{orderId}</keys> 
             <keyType>0</keyType> 
             <addHistoricalData>false</addHistoricalData> 
             <onlyTracking>false</onlyTracking> 
          </ship:queryShipment > 
       </soapenv:Body> 
    </soapenv:Envelope> """
    response = requests.post(url=cargoUrl, data=queryShipmentBody, headers=cargoHeaders)
    if response.status_code == 200:
        print("track")
    return False


def testCreateShipment(orderId):
    value = randint(15000000000, 2500000000000)
    testCreateShipment = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices">
           <soapenv:Header/>
           <soapenv:Body>
              <ship:createShipment>
                 <wsUserName>YKTEST</wsUserName><wsPassword>YK</wsPassword><userLanguage>TR</userLanguage>
              <ShippingOrderVO><cargoKey>{orderId}</cargoKey><invoiceKey>{orderId}</invoiceKey><receiverCustName>ALICI ADI</receiverCustName><receiverAddress>ALICI SEVK ADRESi Kargo Plaza K:5 Maslak</receiverAddress><cityName>istanbul</cityName><townName>sisli</townName><receiverPhone1>2123652365</receiverPhone1><taxOfficeId/><cargoCount>1</cargoCount><specialField1>1$1340965#</specialField1><ttDocumentId/><dcSelectedCredit/><dcCreditRule/><orgReceiverCustId>11988</orgReceiverCustId></ShippingOrderVO></ship:createShipment>
           </soapenv:Body>
        </soapenv:Envelope>"""

    response = requests.post(url=cargoUrl, data=testCreateShipment, headers=cargoHeaders)
    if response.status_code == 200:
        try:
            obj = xmltodict.parse(response.content)
            result = obj["env:Envelope"]["env:Body"]["ns1:createShipmentResponse"]["ShippingOrderResultVO"]["outFlag"]
            if result != '0':
                return False

            return True
        except Exception as e:
            print(e)

def testQueryShipment(orderId,userNameGO,passwordGO):
    testqueryshipment = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices"> 
       <soapenv:Header/> 
       <soapenv:Body> 
          <ship:queryShipment> 
             <wsUserName>{userNameGO}</wsUserName><wsPassword>{passwordGO}</wsPassword><wsLanguage>TR</wsLanguage> 
             <keys>{orderId}</keys> 
             <keyType>0</keyType> 
             <addHistoricalData>false</addHistoricalData> 
             <onlyTracking>false</onlyTracking> 
          </ship:queryShipment > 
       </soapenv:Body> 
    </soapenv:Envelope> """
    response = requests.post(url=cargoUrl, data=testqueryshipment, headers=cargoHeaders)
    if response.status_code == 200:
        try:
            obj = xmltodict.parse(response.content)
            result = obj['env:Envelope']['env:Body']['ns1:queryShipmentResponse']['ShippingDeliveryVO']['outFlag']
            if result != '0':
                return False
            if obj['env:Envelope']['env:Body']['ns1:queryShipmentResponse']['ShippingDeliveryVO']['shippingDeliveryDetailVO']['operationCode']=='0':
                arr = {'cargoKey' : orderId,'response' : "KargoIslemGormemis",'kargoStatusStr' : "KargoIslemGormemis"}
                return arr
            elif obj['env:Envelope']['env:Body']['ns1:queryShipmentResponse']['shippingDeliveryDetailVO']['operationCode']=='1':
                trackingUrl =obj['env:Envelope']['env:Body']['ns1:queryShipmentResponse']['shippingDeliveryDetailVO']['shippingDeliveryItemDetailVO']['trackingUrl']
                arr = {'cargoKey': orderId, 'response': trackingUrl,'kargoStatusStr' : "kargodanTakipNoGeldi"}
                return arr
            else:
                return False
        except Exception as e:
            obj = xmltodict.parse(response.content)
            if obj['env:Envelope']['env:Body']['ns1:queryShipmentResponse']['ShippingDeliveryVO']['shippingDeliveryDetailVO']['errCode'] == '82519':
                arr = {'cargoKey': orderId, 'response': "boyleBirKargoYok", 'kargoStatusStr': "BoyleBirKargoYok"}
                return arr
            print(e)



