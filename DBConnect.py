import mysql.connector as myc
class dbconnection:

    def getconnection(self) -> myc.connection:
        try:
            connection = myc.connect(host="localhost", user="root", password="mysql@shriram1!", database="sys")
            return connection
        except myc.Error as err:
            print(format(err))

    def setdata(self, connection: myc.connection, sql: str, values: str):
        try:
            cursor = connection.cursor()
            cursor.execute(sql, values)
            connection.commit()
        except myc.Error as err:
            print("Error inserting data " + err.msg)

    def getdata(self):
        try:
            connection = self.getconnection()
            cursor = connection.cursor()
            cursor.execute("select * from Employee;")
            data = cursor.fetchone()
            count = cursor.rowcount
            print("no of recs ",count)
            for i in data:
                print(i)
        except myc.Error as err:
            print("Error reading data " + err.msg)