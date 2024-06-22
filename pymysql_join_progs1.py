# sql join:
# 1.Inner join
# 2.left join
# 3.right join
# 4.equi join
import pymysql as pms1

mysql1 = pms1.connect(
    host="localhost",
    user="root",
    password="dragon"
)

table_create1 = """create table test_table1(
id int primary key,
product varchar(20),
price varchar(20)
)"""
table_create2 = """create table test_table2(
id int primary key,
product varchar(22),
quantity int
)"""
mycursor1 = mysql1.cursor()
mycursor1.execute("DROP DATABASE IF EXISTS PYSQL2")
mycursor1.execute("CREATE DATABASE PYSQL2")
mycursor1.execute("USE PYSQL2")
mycursor1.execute("DROP TABLE IF EXISTS test_table1")
mycursor1.execute("DROP TABLE IF EXISTS test_table2")
mycursor1.execute(table_create1)
mycursor1.execute(table_create2)
sql1 = "insert into test_table1(id, product, price) values(%s,%s,%s)"
data1 = [(2, "orange", "7.5"), (3, "pineapple", "9.0"),
         (4, "mango", "15.5"), (5, "squash", "5.2")]
# try:
mycursor1.executemany(sql1, data1)
mysql1.commit()
print("Table1 successful")
mycursor1.execute("select * from test_table1")
sdata1 = mycursor1.fetchall()
print("{:<20}{:<20}{:<20}".format("id", "product", "price"))
for s1 in sdata1:
    print("{:<20}{:<20}{:<20}".format(s1[0], s1[1], s1[2]))
# except:
    # print("ErrorT1!")
sql1 = "insert into test_table2(id, product,quantity) values(%s,%s,%s)"
data1 = [(1, "apple", "10.1"), (3, "pineapple", "90"),
         (4, "mango", "400"), (5, "squash", "1000")]
# try:
mycursor1.executemany(sql1, data1)
mysql1.commit()
print("Table2 successful")
mycursor1.execute("select * from test_table2")
sdata1 = mycursor1.fetchall()
print("{:<20}{:<20}{:<20}".format("id", "product", "quantity"))
for s1 in sdata1:
    print("{:<20}{:<20}{:<20}".format(s1[0], s1[1], s1[2]))
# except:
    # print("ErrorT2!")
print("Inner Join")
sql1 = "select * from test_table1 inner join test_table2 on test_table1.id = test_table2.id"
mycursor1.execute(sql1)
sdata1 = mycursor1.fetchall()
for s1 in sdata1:
    print(s1)
print("left Join")
sql1 = "select * from test_table1 left join test_table2 on test_table1.id = test_table2.id"
mycursor1.execute(sql1)
sdata1 = mycursor1.fetchall()
for s1 in sdata1:
    print(s1)
print("right Join")
sql1 = "select * from test_table right join test_table2 on test_table1.id = test_table2.id"
mycursor1.execute(sql1)
sdata1 = mycursor1.fetchall()
for s1 in sdata1:
    print(s1)
print("equi Join")
sql1 = "select * from test_table1 join test_table2 on test_table1.id = test_table2.id"
mycursor1.execute(sql1)
sdata1 = mycursor1.fetchall()
for s1 in sdata1:
    print(s1)
print("equi Join")
sql1 = "select * from test_table1, test_table2 where test_table1.id = test_table2.id"
mycursor1.execute(sql1)
sdata1 = mycursor1.fetchall()
for s1 in sdata1:
    print(s1)
