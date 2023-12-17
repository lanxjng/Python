import mysql.connector

# Kết nối đến MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3308,
    database="ukb"
)

# Tạo database "ukb" nếu chưa tồn tại

# sql = ("CREATE DATABASE IF NOT EXISTS ukb")
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# Tạo bảng nhanvien
# sql = ('CREATE TABLE IF NOT EXISTS nhanvien (mavn INT PRIMARY KEY,'
#        'tennv VARCHAR(40) NOT NULL, gioitinh VARCHAR(10) NOT NULL)')
# mycursor = mydb.cursor()
# mycursor.execute(sql)
#
#
# # Thêm 3 bản ghi vào bảng nhanvien
#
# sql = "INSERT INTO nhanvien (mavn, tennv, gioitinh) VALUES (%s,%s,%s) "
# data = [
#     (1, 'Nguyen Van A', 'Nam'),
#     (2, 'Tran Thi B', 'Nu'),
#     (3, 'Le Van C', 'Nam')
# ]
# mycursor = mydb.cursor()
# mycursor.executemany(sql,data)
# mydb.commit()
# print(f"So dong duoc them vao bang:  {mycursor.rowcount}")

sql = "SELECT * FROM nhanvien"
mycursor = mydb.cursor()
mycursor.execute(sql)
# students = mycursor.fetchall()
# students = mycursor.fetchmany(5)
for x in mycursor:
	print(x)