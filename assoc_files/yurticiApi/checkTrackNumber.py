import threading
from assoc_files.yurticiApi.cargoApi import testQueryShipment
from assoc_files.database.modal import OrderTable


def checkTrackNumber():
  #threading.Timer(20, checkTrackNumber).start()
  try:

    orderIdStatus2 = []
    orders = OrderTable.query.filter_by(orderStatus=2).all()
    print(orders,"orders")
    for i in orders:
      orderIdStatus2.append(int(i.orderId))
    print(orderIdStatus2)

    for j in orderIdStatus2:
      result = testQueryShipment(orderId=j)
      if result['cargoKey'] in orderIdStatus2:
        order = OrderTable.query.filter_by(orderId=result['cargoKey']).one_or_none()
        order.cargoUrl = result


  except Exception as e:
    print(e)
    return False



checkTrackNumber()



