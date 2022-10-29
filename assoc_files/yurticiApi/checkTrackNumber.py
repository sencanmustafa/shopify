import threading
from flask import session
from assoc_files.yurticiApi.cargoApi import testQueryShipment
from assoc_files.database.modal import OrderTable, YurticiKargoApiInfo


def checkTrackNumber():
  #threading.Timer(240, checkTrackNumber).start()
  try:
    yurticiUser = YurticiKargoApiInfo.query.filter_by(userId=session["userId"]).one_or_none()
    yurticiUsernameGO = yurticiUser.userNameForGO
    yurticiPasswordGO = yurticiUser.userPasswordForGO
    orderIdStatus2 = []
    orders = OrderTable.query.filter_by(userId=session["userId"],orderStatus=2).all()
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
    return True
  except Exception as e:
    print(e)
    return False







