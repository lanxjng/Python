import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3308,
    database="qlsv"
)
# sql = "SELECT * FROM student WHERE(`full_name` like '%Th%')"
# mycursor = mydb.cursor()
# mycursor.execute("DROP DATABASE lancho3")
# mycursor.execute("DROP TABLE subject1")

# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
# 	print(x)

# sql = "CREATE DATABASE ukb"
# mycursor = mydb.cursor()
# mycursor.execute(sql)

# sql = "DROP DATABASE ukb"
# mycursor = mydb.cursor()
# mycursor.execute(sql)
#
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
# 	print(x)

# sql = "SELECT * FROM student"
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# students = mycursor.fetchall()
# for x in students:
# 	print(x)

# sql = ('CREATE TABLE subject (id INT AUTO_INCREMENT PRIMARY KEY,'
#        'name VARCHAR(40) NULL, credit INT NULL)')
# mycursor = mydb.cursor()
# mycursor.execute(sql)

# sql = ('ALTER TABLE subject '
#        'AUTO_INCREMENT = 100')
# mycursor = mydb.cursor()
# mycursor.execute(sql)

# sql = ('ALTER TABLE subject '
#        'ADD COLUMN lesson INT NOT NULL')
# mycursor = mydb.cursor()
# mycursor.execute(sql)

# sql = "INSERT INTO subject VALUES ('3', 'Man Thi Lann',25,3)"
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# mydb.commit()
# sql = "SHOW TABLES"
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# for x in mycursor:
# 	print(x)

# sql = "SELECT * FROM student"
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# # students = mycursor.fetchall()
# # students = mycursor.fetchmany(5)
# for x in mycursor:
# 	print(x)
# a = "Th"
# b = "6 or 1=1;--"
# sql = f"SELECT * FROM student WHERE full_name like '%{a}%' AND gpa >={b}"
# # data = ('%Th%',3.65)
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# for x in mycursor:
# 	print(x)

# sql = "INSERT INTO student (id, full_name, email, gpa, major) VALUES (%s,%s,%s,%s,%s) "
# data = [('SV1018', 'Trần Trọng Anhhhh', 'tronganh@xmail.com', 3.0, 'CNTT'),
#         ('SV10077', 'Mã Đại Hải', 'madaihai@xmail.com', 3.85, 'CNTT')]
# mycursor = mydb.cursor()
# mycursor.executemany(sql,data)
# mydb.commit()
# print(f"So dong duoc them vao bang:  {mycursor.rowcount}")

# sql = "UPDATE student SET gpa = %s WHERE id = %s "
# data = (3.5,'SV1001')
# mycursor = mydb.cursor()
# mycursor.execute(sql,data)
# mydb.commit()
# print(f"So dong bi thay doi vao bang:  {mycursor.rowcount}")
#
# sql = "DELETE FROM student WHERE  id = %s "
# data = ("SV1015",)
# mycursor = mydb.cursor()
# mycursor.execute(sql,data)
# mydb.commit()
# print(f"So dong bi thay doi vao bang:  {mycursor.rowcount}")
#
# sql = "SELECT * FROM student"
# mycursor = mydb.cursor()
# mycursor.execute(sql)
# # students = mycursor.fetchall()
# # students = mycursor.fetchmany(5)
# for x in mycursor:
# 	print(x)