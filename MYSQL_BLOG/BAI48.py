import mysql.connector

server="localhost"
port=3306
database="studentmanagement"
username="root"
password="@Obama123"

conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)

print("\n(2.1) Truy vấn toàn bộ Sinh viên:")

cursor = conn.cursor()

sql="select * from student"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\n(2.2) Truy vấn các Sinh viên có độ tuổi từ 22 tới 26:")

cursor = conn.cursor()
sql="SELECT * FROM student where Age>=22 and Age<=26"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\n(2.3) Truy vấn toàn bộ sinh viên và sắp xếp theo tuổi tăng dần:")

cursor = conn.cursor()
sql="SELECT * FROM student " \
    "order by Age asc"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\n(2.4) Truy vấn các Sinh viên có độ tuổi từ 22 tới 26 và sắp xếp theo tuổi giảm dần:")

cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where Age>=22 and Age<=26 " \
    "order by Age desc "
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\n(2.5) Truy vấn chi tiết thông tin Sinh viên khi biết Id:")

cursor = conn.cursor()
sql="SELECT * FROM student " \
    "where ID=1 "

cursor.execute(sql)

dataset=cursor.fetchone()
if dataset!=None:
    id,code,name,age,avatar,intro=dataset
    print("Id=",id)
    print("code=",code)
    print("name=",name)
    print("age=",age)

cursor.close()

print("\n(2.6) Truy vấn dạng phân trang Student:")
sql="SELECT * FROM student LIMIT 3 OFFSET 0"
cursor = conn.cursor()
sql="SELECT * FROM student LIMIT 3 OFFSET 0"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\nLần thứ nhì truy vấn 3 dòng dữ liệu còn lại (các ID 4, 5, 6) thì câu SQL viết như sau:")
sql="SELECT * FROM student LIMIT 3 OFFSET 3"

cursor = conn.cursor()
sql="SELECT * FROM student LIMIT 3 OFFSET 3"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))

cursor.close()

print("\nPAGING ")
print("PAGING!!!!!")
cursor = conn.cursor()
sql="SELECT count(*) FROM student"
cursor.execute(sql)
dataset=cursor.fetchone()
rowcount=dataset[0]

limit=3
step=3
for offset in range(0,rowcount,step):
    sql=f"SELECT * FROM student LIMIT {limit} OFFSET {offset}"
    cursor.execute(sql)

    dataset=cursor.fetchall()
    align='{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code','Name',"Age"))
    for item in dataset:
        id=item[0]
        code=item[1]
        name=item[2]
        age=item[3]
        avatar=item[4]
        intro=item[5]
        print(align.format(id,code,name,age))

cursor.close()

print("\n(3.1) Thêm mới 1 Student")

cursor = conn.cursor()

sql="insert into student (code,name,age) values (%s,%s,%s)"

val=("sv07","Đoàn Phương Nghi",87)

cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount," record inserted")

cursor.close()

print("\n(3.2) Thêm mới nhiều Student:")
cursor = conn.cursor()

sql="insert into student (code,name,age) values (%s,%s,%s)"

val=[
    ("sv08","Nguyễn Nhật Huy",318),
    ("sv09","Nguyễn Yến Ngân",227),
    ("sv10","Lê Nguyễn Mỹ Duyên",35)
    ,
     ]

cursor.executemany(sql,val)

conn.commit()

print(cursor.rowcount," record inserted")

cursor.close()

print("\n(4.1) Cập nhật tên Sinh viên có Code=’sv09′ thành tên mới “Hoàng Lão Tà”")

cursor = conn.cursor()
sql="update student set name='Hoàng Lão Tà' where Code='sv09'"
cursor.execute(sql)

conn.commit()

print(cursor.rowcount," record(s) affected")

print("\n(4.2) Cập nhật tên Sinh viên có Code=’sv09′ thành tên mới “Đặng Thị Kim Thuý” như viết dạng SQL Injection:")

cursor = conn.cursor()
sql="update student set name=%s where Code=%s"
val=('Đặng Thị Kim Thuý','sv09')

cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount," record(s) affected")

print("\n(5.1) Xóa Student có ID=14")
conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql="DELETE from student where ID=14"
cursor.execute(sql)

conn.commit()

print(cursor.rowcount," record(s) affected")

print("\n(5.2) Xóa Student có ID=13 với SQL Injection")

conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql = "DELETE from student where ID=%s"
val = (13,)

cursor.execute(sql, val)

conn.commit()

print(cursor.rowcount," record(s) affected")