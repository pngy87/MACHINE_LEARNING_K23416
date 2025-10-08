import traceback

import mysql.connector

server="localhost"
port=3306
database="k23416_retail"
username="root"
password="@Obama123"
#try...except là thông báo lỗi nhưng phần chạy tiếp tục ra sau cái lỗi đó
try:
    conn = mysql.connector.connect(
                    host=server,
                    port=port,
                    database=database,
                    user=username,
                    password=password)
except:
    traceback.print_exc() #thông báo chi tiết lỗi ra
print("---Tiếp tục phần mềm---")
print("--CRUD--")
# Câu 1: Đăng nhập cho Customer
def login_customer(email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
    "where Email = '"+email + "'and Password ='"+pwd+"'"
    cursor.execute(sql)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed")
    cursor.close()
login_customer("daodao@gmail.com", "123")

def login_employee(email, pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM employee " \
          "where Email =%s and Password=%s"
    val=(email,pwd)
    cursor.execute(sql, val)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed")
    cursor.close()
login_employee("kim@yahoo.com", "123")


