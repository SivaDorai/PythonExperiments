from datetime import datetime as datetime
from DBConnect import dbconnection
import time

class Order:
    orderid: str
    orderdate: time
    quantity: int
    scrip: str
    price: float
    status: str
    def __init__(self, orderid: int,orderdate:time,quantity:int, scrip:str, price:float, status:str ):
        self.orderid = orderid
        self.orderdate = orderdate
        self.quantity = quantity
        self.price = price
        self.scrip = scrip
        self.status = status

    def createorder(self):
        dbc = dbconnection()
        con = dbc.getconnection()
        sql = ("INSERT INTO order "
               "(orderid, orderdate, scrip, quantity, price, status) "
               " VALUES (%s, %s,%s,%s,%s,%s)")
        values = (self.orderid, self.orderdate, self.scrip, self.quantity, self.price, self.status)
        dbc.setdata(con, sql, values)

ordertime = time.strftime('%Y-%m-%d %H:%M:%S')
order1 = Order( 1,ordertime,100,"RIL",2500.00,"Open")
order1.createorder()
print(order1.scrip+ " order created at " + str(order1.orderdate))