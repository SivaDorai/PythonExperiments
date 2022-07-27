import mysql.connector as myc
mydb = myc.connect(host="localhost", user="root", password="mysql@shriram1!", database="sys")
cursor = mydb.cursor()
cursor.execute("select * from Employee;")
data = cursor.fetchone()
count = cursor.rowcount
print("no of recs ",count)
for i in data:
    print(i)