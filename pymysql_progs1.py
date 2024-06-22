# 1.pip  pymsql
#    to install it ->" pip install pymysql"
#    if update required->"python.exe -m pip install --upgrade pip"2
# 2.Xampp installation
#         download Xampp / MySQL WORK bench
#         browse-> localhost/phpmyadmin/ a

# DATA TYPE:
# int ->(11numbers)
# big int->(20numbers)
# text  ->(0-6000char)
# varchar ->(0-255char)
# longtext
# date ->(yyyy-mm-dd)->(2010-08-12)
# dateTime
# time stamp->(yyyy-mm-dd,ha-min-ss)
# tinyint-> (3numbers )
# time->(hh-mm-ss)
# year->(yyyy)


import pymysql as pms1

mysql1 = pms1.connect(
    host="localhost",
    user="root",
    passwd="dragon"
)
mycursor1 = mysql1.cursor()
# mycursor1.execute("DROP DATABASE IF EXISTS PYSQL1")
mycursor1.execute("DROP DATABASE IF EXISTS PYSQL2")
mycursor1.execute("create database PYSQL2")
mycursor1.execute("use PYSQL2")
print("Database Created Successfully")
mysql1.close()

# Create a connection object
# IP address of the MySQL database server
# Host = "localhost"
# User name of the database server
# User = "user"
# Password for the database user
# Password = ""
# conn  = pymysql.connect(host=Host, user=User, password=Password)
# Create a cursor object
# cur  = conn.cursor()
# creating database
# cur.execute("CREATE DATABASE GFG")
# cur.execute("SHOW DATABASES")
# databaseList = cur.fetchall()
# for database in databaseList:
# print(database)
# conn.close()

mysql1 = pms1.connect(
    host="localhost",
    user="root",
    passwd="dragon",
    database="PYSQL2"
)
mycursor1 = mysql1.cursor()
table_create1 = """create table student1(
st_id int primary key auto_increment,
st_name varchar(30),
st_class varchar(10),
st_email varchar(20)
)"""
mycursor1.execute(table_create1)
# insert one data
ins1 = "insert into student1(st_name, st_class, st_email) values(%s,%s,%s)"
data1 = ('Rajiv Singh', '10th', 'rajiv12@gmail.com')
try:
    mycursor1.execute(ins1, data1)
    mysql1.commit()
    print("Data inserted successfully")
except:
    print("Error!")
ins2 = "insert into student1(st_name, st_class, st_email) values('R1 S1', '10th', 'r1s1@gmail.com')"
mycursor1.execute(ins2)
mysql1.commit()
ins2 = "insert into student1 values(5,'R2 S2', '10th', 'r2s2@gmail.com')"
mycursor1.execute(ins2)
mysql1.commit()
# insert multiple data
ins1 = "insert into student1(st_name,st_class,st_email) values(%s,%s,%s)"
data1 = [("Ajit Kumar", "12th", "ajit22@gmail.com"), ("Rahul Sen",
                                                      '10th', "rahul100@gmail.com"), ('Ram Setu', '9th', 'ramram@ram.com')]
try:
    mycursor1.executemany(ins1, data1)
    mysql1.commit()
    print("Multiple data inserted successfully")
except:
    print("Error!")
# display

mycursor1.execute("select * from student1")
sdata1 = mycursor1.fetchall()
for s1 in sdata1:
    print(s1)
mycursor1.execute("select * from student1")
sdata1 = mycursor1.fetchmany(3)
for s1 in sdata1:
    print(s1)
mycursor1.execute("select * from student1")
sdata1 = mycursor1.fetchone()
while sdata1 is not None:
    print(sdata1)
    sdata1 = mycursor1.fetchone()

try:
    mycursor1.execute("select * from student1")
    sdata1 = mycursor1.fetchall()
    for s1 in sdata1:
        print(s1)
    print("\n\n")
    print("{:^20}{:^30}{:^15}{:^30}".format("Student ID",
          "Student Name", "Student Class", "Student email"))
    for s1 in sdata1:
        print("{:^20}{:^30}{:^15}{:^30}".format(s1[0], s1[1], s1[2], s1[3]))
except:
    print("Error!")
print()
print("{:<20}{:<30}".format("Student ID", "Student Name"))
sql1 = "select st_id,st_name from student1"
try:
    mycursor1.execute(sql1)
    sdata1 = mycursor1.fetchall()
    for s1 in sdata1:
        print("{:<20}{:<30}".format(s1[0], s1[1]))
except:
    print("Error!")
mysql1.close()
# update
mysql1 = pms1.connect(
    host="localhost",
    user="root",
    passwd="dragon",
    database="PYSQL2"
)
mycursor1 = mysql1.cursor()
# student_id1 = input("Enter student id: ")
# student_name1 = input("Enter the name: ")
# student_class1 = input("Enter the class: ")
# student_email1 = input("Enter student email: ")
sql1 = "update student1 set st_name=%s,st_class=%s,st_email=%s where st_id=%s"
# data1 = (student_name1,student_class1,student_email1,student_id1)
# try:
#   mycursor1.execute(sql1,data1)
#   mysql1.commit()
#   print("Data updated successfully")
# except:
#   print("Error!")
# sort
print("{:<20}{:<30}{:<15}{:<30}".format("Student ID",
      "Student Name", "Student Class", "Student_email"))
sql1 = "select * from student1 order by st_name desc"  # ASC DESC
try:
    mycursor1.execute(sql1)
    sdata1 = mycursor1.fetchall()
    for s1 in sdata1:
        print("{:<20}{:<30}{:<15}{:<30}".format(s1[0], s1[1], s1[2], s1[3]))
except:
    print("Error!")
# limit
mycursor1.execute("select * from student1")
sdata1 = mycursor1.fetchall()
print("aaa")
for s1 in sdata1:
    print(s1)
print("a{:<20}{:<30}{:<15}{:<30}".format("Student ID",
      "Student Name", "Student Class", "Student email"))
# offset is no of rows to skip, limit is no of rows to print
sql1 = "select * from student1 order by st_id asc limit 3 offset 2"
# "select distinct * from student1 order by st_id desc limit 2,3"
try:
    mycursor1.execute(sql1)
    sdata1 = mycursor1.fetchall()
    for s1 in sdata1:
        print(s1)
        # print("{:<20}{:<30}{:<15}{:<30}".format(s1[0],s1[1],s1[2],s1[3]))
except:
    print("Error")
# searching and filter
student_name1 = input("Enter student name: ")
print("{:<20}{:<30}{:<15}{:<30}".format("Student ID",
      "Student Name", "Student Class", "Student email"))
sql1 = "select * from student1 where st_name='%"+student_name1+"%'"

try:
    mycursor1.execute(sql1)
    sdata1 = mycursor1.fetchall()
    for s1 in sdata1:
        print("{:<20}{:<30}{:<15}{:<30}".format(s1[0], s1[1], s1[2], s1[3]))
except:
    print("Error!")
# like --- single input
student_name1 = input("Enter student name: ")
print("{:<20}{:<30}{:<15}{:<30}".format("Student ID",
      "Student Name", 'Student Class', "Student email"))
sql1 = "select * from student1 where st_name like'%"+student_name1+"%'"
try:
    mycursor1.execute(sql1)
    sdata1 = mycursor1.fetchall()
    for s1 in sdata1:
        print("{:<20}{:<30}{:<15}{:<30}".format(s1[0], s1[1], s1[2], s1[3]))
except:
    print("Error!")
# like --- multiple input
student_name1 = input("Enter the name: ")
student_class1 = input("Enter the class: ")
print("{:<20}{:<30}{:<15}{:<30}".format("Student ID",
      "Student Name", "Student Class", "Student email"))
sql1 = "select * from student1 where st_name like'%" + \
    student_name1+"%'and st_class like'%"+student_class1+"%'"
try:
    mycursor1.execute(sql1)
    sdata1 = mycursor1.fetchall()
    for s1 in sdata1:
        print("{:<20}{:<30}{:<15}{:<30}".format(s1[0], s1[1], s1[2], s1[3]))
except:
    print('Error!')
mysql1.close()


# delete row
mysql1 = pms1.connect(
    host="localhost",
    user="root",
    passwd="dragon",
    database="PYSQL2"
)
mycursor1 = mysql1.cursor()
sql1 = "delete from student1 where st_id=%s"
student_id1 = input("Enter the student id: ")
try:
    mycursor1.execute(sql1, student_id1)
    mysql1.commit()
    print("Data deleted succesfully")
except:
    print("Error!")

table_create1 = """create table test_table1(
id int primary key auto_increment,
product varchar(20),
price varchar(20)
)"""
table_create2 = """create table test_table2(
id int  auto_increment primary key,
product varchar(22),
quantity int
)"""
mycursor1.execute("DROP TABLE IF EXISTS test_table1")
mycursor1.execute("DROP TABLE IF EXISTS test_table2")
mycursor1.execute(table_create1)
mycursor1.execute(table_create2)
sql1 = "insert into test_table1(product, price) values(%s,%s)"
data1 = [("apple", "10.1"), ("orange", "7.5"), ("pineapple", "9.0"),
         ("mango", "15.5"), ("squash", "5.2")]
try:
    mycursor1.executemany(sql1, data1)
    mysql1.commit()
    print("Table1 successful")
    mycursor1.execute("select * from test_table1")
    sdata1 = mycursor1.fetchall()
    print("{:<20}{:<20}{:<20}".format("id", "product", "price"))
    for s1 in sdata1:
        print("{:<20}{:<20}{:<20}".format(s1[0], s1[1], s1[2]))
except:
    print("ErrorT1!")
sql1 = "insert into test_table2(product,quantity) values(%s,%s)"
data1 = [("apple", "200"), ("orange", "250"), ("pineapple", "90"),
         ("mango", "400"), ("squash", "1000")]
try:
    mycursor1.executemany(sql1, data1)
    mysql1.commit()
    print("Table2 successful")
    mycursor1.execute("select * from test_table2")
    sdata1 = mycursor1.fetchall()
    print("{:<20}{:<20}{:<20}".format("id", "product", "quantity"))
    for s1 in sdata1:
        print("{:<20}{:<20}{:<20}".format(s1[0], s1[1], s1[2]))
except:
    print("ErrorT2!")
# truncate table
try:
    mycursor1.execute("truncate table test_table1")
    print("test_table1 truncated")
    mycursor1.execute("select * from test_table1")
    sdata1 = mycursor1.fetchall()
    print("{:<20}{:<20}{:<20}".format("id", "product", "price"))
    for s1 in sdata1:
        print("{:<20}{:<20}".format(s1[0], s1[1], s1[2]))
except:
    print("ErrorTT1!")
# drop table
try:
    mycursor1.execute("drop table test_table2")
    print("test_table2 dropped")
except:
    print("ErrorDT2!")
mysql1.close()

# drop database
mysql1 = pms1.connect(
    host="localhost",
    user="root",
    passwd="dragon",
    database="PYSQL2"
)
try:
    mycursor1 = mysql1.cursor()
    mycursor1.execute("drop database PYSQL2")
    print("PYSQL2 deleted")
except:
    print("ErrorDD!")
mysql1.close()
