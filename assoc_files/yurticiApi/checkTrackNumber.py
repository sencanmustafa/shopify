import threading

from assoc_files.utilities.order import sendTagShipping
from assoc_files.yurticiApi.cargoApi import testQueryShipment
from assoc_files.database.modal import OrderTable,ShopInformationTable


def checkTrackNumber():
  threading.Timer(240, checkTrackNumber).start()
  try:
    yurticiUser = ShopInformationTable.query.all()
    for x in yurticiUser:
      yurticiUsernameGO = x.userNameForGO
      yurticiPasswordGO = x.userPasswordForGO
      orderIdStatus2 = []
      orders = OrderTable.query.filter_by(userId=x.userId,orderStatus=2).all()
      print(orders,"orders")
      for i in orders:
        orderIdStatus2.append(int(i.orderId))
      print(orderIdStatus2)
#
      for j in orderIdStatus2:
        result = testQueryShipment(orderId=j,userNameGO=yurticiUsernameGO,passwordGO=yurticiPasswordGO)
        print("********")
        print(result)
        #### CODE DUPLICATION ######## CODE DUPLICATION ######## CODE DUPLICATION ######## CODE DUPLICATION ####
        if result['cargoKey'] in orderIdStatus2 and result['kargoStatusStr'] == 'kargodanTakipNoGeldi' :
          try:
            order = OrderTable.query.filter_by(orderId=result['cargoKey']).one_or_none()
            order.cargoUrl = result['response']
            order.orderStatus = 3
            order.orderStatusStr = result['kargoStatusStr']
            OrderTable.updateTable(order)
            sendTagShipping(orderId=order.orderId)
            print("success")
            continue
          except Exception as e:
            print(e)
            return False
        elif result['cargoKey'] in orderIdStatus2 and result['kargoStatusStr'] == 'KargoIslemGormemis':
          try:
            order = OrderTable.query.filter_by(orderId=result['cargoKey']).one_or_none()
            order.cargoUrl = result['response']
            order.orderStatus = 2
            order.orderStatusStr = result['kargoStatusStr']
            OrderTable.updateTable(order)
            print("success")
            continue
          except Exception as e:
            print(e)
            return False
        elif result['cargoKey'] in orderIdStatus2 and result['kargoStatusStr'] == 'BoyleBirKargoYok':
          try:
            order = OrderTable.query.filter_by(orderId=result['cargoKey']).one_or_none()
            order.cargoUrl = result['response']
            order.orderStatus = 2
            order.orderStatusStr = result['kargoStatusStr']
            OrderTable.updateTable(order)
            print("success")
            continue
          except Exception as e:
            print(e)
            return False
        #### CODE DUPLICATION ######## CODE DUPLICATION ######## CODE DUPLICATION ######## CODE DUPLICATION ####
        else:
          return False
      continue
    return True
  except Exception as e:
    print(e)
    return False







