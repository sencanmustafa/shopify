import requests , xmltodict
from assoc_files.database.modal import *
from sqlalchemy import desc
cargoUrl="http://testwebservices.yurticikargo.com:9090/KOPSWebServices/ShippingOrderDispatcherServices?wsdl "
cargoHeaders = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}
queryShipmentBody = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices"> 

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
createShipmentBody = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ship="http://yurticikargo.com.tr/ShippingOrderDispatcherServices">

   <soapenv:Header/>

   <soapenv:Body>

      <ship:createShipment>

         <wsUserName>YKTEST</wsUserName><wsPassword>YK</wsPassword><userLanguage>TR</userLanguage>

      <ShippingOrderVO><cargoKey>4525184187541589</cargoKey><invoiceKey>4525184187541589</invoiceKey><receiverCustName>ALICI ADI</receiverCustName><receiverAddress>ALICI SEVK ADRESi Kargo Plaza K:5 Maslak</receiverAddress><cityName>istanbul</cityName><townName>sisli</townName><receiverPhone1>2123652365</receiverPhone1><taxOfficeId/><cargoCount>1</cargoCount><specialField1>1$1340965#</specialField1><ttDocumentId/><dcSelectedCredit/><dcCreditRule/><orgReceiverCustId>11988</orgReceiverCustId></ShippingOrderVO></ship:createShipment>

   </soapenv:Body>

</soapenv:Envelope>"""




#response = requests.post(url=cargoUrl,data=createShipmentBody,headers=cargoHeaders)
#obj = xmltodict.parse(response.content)
#
#print(obj)


