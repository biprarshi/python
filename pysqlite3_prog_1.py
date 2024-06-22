# from os import remove
import pysqlite3


conn1 = pysqlite3.connect("student1.db")
curs1 = conn1.cursor()
curs1.execute("DROP TABLE IF EXISTS student_table1")
curs1.execute('''CREATE TABLE student_table1(
     st_id UNSIGNED BIG INT AUTO_INCREMENT PRIMARY KEY ,
     st_name VARCHAR(50),
     st_class VARCHAR(10),
     st_email VARCHAR(10)
)''')


# INSERT DATA:
insert1 = '''INSERT INTO student_table1 (st_id,st_name,st_class,st_email) 
VALUES (7,"Avijit Kumar","12th","avi@gmail.com")
'''
curs1.execute(insert1)
insert2 = "INSERT INTO student_table1 VALUES (?, ?, ?, ?)"
data2 = [(8, "aaa", "11th", "aaa@gmail.com"),
         (9, "bbb", "12th", "bbb@gmail.com"),
         (5, "ccc", "10th", "ccc@gmail.com"),
         (13, "zzza", "13th", "zzz@yahoo.com")]

curs1.executemany(insert2, data2)
conn1.commit()
conn1.close()
print("Data inserted successfully")

# # # FETCHING DATA
conn2 = pysqlite3.connect("student1.db")
curs2 = conn2.cursor()
data1 = curs2.execute("SELECT * FROM student_table1")
for n in data1:
    print(n)
    # print(n[0], n[1], n[2], n[3])
print()
# no of rows to skip(OFFSET=1) no of rows(LIMIT=3)
data2 = curs2.execute("SELECT * FROM student_table1 LIMIT 1, 3")
for n in data2:
    print(n)
print()
# data2 = curs2.execute("SELECT * FROM student_table1 LIMIT 3 OFFSET 1")
# for n in data2:
#     print(n)


conn2.close()


conn1 = pysqlite3.connect("student1.db")
curs1 = conn1.cursor()
curs1.execute("DROP TABLE IF EXISTS fees1")
curs1.execute("""CREATE TABLE fees1(
    fees_id INT NOT NULL,
    st_id INT NOT NULL,
    st_fees INT,
    FOREIGN KEY (st_id)
    REFERENCES student_table1 (st_id)
)""")


insert3 = """INSERT INTO fees1 (fees_id,st_id,st_fees)
VALUES (105,5,3200)
"""
curs1.execute(insert3)
conn1.commit()
conn1.close()


conn1 = pysqlite3.connect("student1.db")
curs1 = conn1.cursor()
print(5)
data1 = curs1.execute("SELECT * FROM student_table1 WHERE st_id=5")
# data1 = curs1.execute("SELECT * FROM student_table1 WHERE st_id LIKE '%"+"5"+"%'")
for n in data1:
    print(n, "wow")
st_name1 = input("Enter Name: ")
st_class1 = input("Enter Class: ")
data1 = curs1.execute(
    "SELECT * FROM student_table1 WHERE st_name like '%"+st_name1+"%'")
for i in data1:
    print(i)
# data1 = curs1.execute("SELECT * FROM student_table1 WHERE st_name LIKE '%"+st_name1+"%' OR st_class LIKE '%"+st_class1+"%'")
# for i in data1:
#     print(i)
print()
data1 = curs1.execute("SELECT * FROM student_table1 WHERE st_class LIKE '%" +
                      st_class1+"%' AND st_name LIKE '%"+st_name1+"%'")
for i in data1:
    for j in i:
        print(j, end=' ')
    print()
data1 = curs1.execute("SELECT * FROM student_table1 WHERE st_class LIKE '%" +
                      st_class1+"%' AND st_name LIKE '%"+st_name1+"%' AND st_email LIKE '%"+"yahoo"+"%'")
for x1 in data1:
    print(x1)
conn1.close()

# remove("student1.db")


# The following table shows how many common datatype names from more traditional SQL implementations are converted into affinities by the five rules of the previous section.
# This table shows only a small subset of the datatype names that SQLite will accept.
# Note that numeric arguments in parentheses that following the type name(ex: "VARCHAR(255)") are ignored by SQLite -
# SQLite does not impose any length restrictions (other than the large global SQLITE_MAX_LENGTH limit) on the length of strings, BLOBs or numeric values.


# Determination Of Column Affinity
# Any column can still store any type of data. It is just that some columns, given the choice, will prefer to use one storage class over another. The preferred storage class for a column is called its "affinity".
# Example Typenames From The
# CREATE TABLE Statement
# or CAST Expression	                    Resulting Affinity                  Rule Used To Determine Affinity

# INT                                     INTEGER	                            1
# INTEGER
# TINYINT
# SMALLINT
# MEDIUMINT
# BIGINT
# UNSIGNED BIG INT
# INT2
# INT8
# CHARINT

# CHARACTER(20)                           TEXT	                            2
# VARCHAR(255)
# VARYING CHARACTER(255)
# NCHAR(55)
# NATIVE CHARACTER(70)
# NVARCHAR(100)
# TEXT
# CLOB

# BLOB                                    BLOB	                            3
# no datatype specified

# REAL                                    REAL	                            4
# DOUBLE
# DOUBLE PRECISION
# FLOAT

# NUMERIC                                 NUMERIC	                            5
# DECIMAL(10,5)
# BOOLEAN
# DATE
# DATETIME

# Each value stored in an SQLite database (or manipulated by the database engine) has one of the following storage classes:

# NULL. The value is a NULL value.
# INTEGER. The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
# REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
# TEXT. The value is a text string, stored using the database encoding(UTF-8, UTF-16BE or UTF-16LE).
# BLOB. The value is a blob of data, stored exactly as it was input.
# A storage class is more general than a datatype. The INTEGER storage class, for example, includes 7 different integer datatypes of different lengths. This makes a difference on disk.
# But as soon as INTEGER values are read off of disk and into memory for processing, they are converted to the most general datatype (8-byte signed integer).
# And so for the most part, "storage class" is indistinguishable from "datatype" and the two terms can be used interchangeably.
# Any column in an SQLite version 3 database, except an INTEGER PRIMARY KEY column, may be used to store a value of any storage class .
# All values in SQL statements, whether they are literals embedded in SQL statement text or parameters bound to precompiled SQL statements have an implicit storage class .
# Under circumstances described below, the database engine may convert values between numeric storage classes(INTEGER and REAL) and TEXT during query execution.


# Maximum length of a string or BLOB
# The maximum number of bytes in a string or BLOB in SQLite is defined by the preprocessor macro SQLITE_MAX_LENGTH. The default value of this macro is 1 billion (1 thousand million or 1, 000,000,000).


# Most SQL database engines(every SQL database engine other than SQLite, as far as we know) uses static, rigid typing. With static typing, the datatype of a value is determined by its container -
# the particular column in which the value is stored.
# SQLite uses a more general dynamic type system. In SQLite, the datatype of a value is associated with the value itself, not with its container.
# The dynamic type system of SQLite is backwards compatible with the more common static type systems of other database engines in the sense that SQL statements that work on statically typed databases work the same way in SQLite.
# However, the dynamic typing in SQLite allows it to do things which are not possible in traditional rigidly typed databases. Flexible typing is a feature of SQLite, not a bug.
# For tables not declared as STRICT, the affinity of a column is determined by the declared type of the column, according to the following rules in the order shown:
# If the declared type contains the string "INT" then it is assigned INTEGER affinity.
# If the declared type of the column contains any of the strings "CHAR", "CLOB", or "TEXT" then that column has TEXT affinity. Notice that the type VARCHAR contains the string "CHAR" and is thus assigned TEXT affinity.
# If the declared type for a column contains the string "BLOB" or if no type is specified then the column has affinity BLOB.
# If the declared type for a column contains any of the strings "REAL", "FLOA", or "DOUB" then the column has REAL affinity.
# Otherwise, the affinity is NUMERIC.

# STRICT
# CREATE TABLE t1(a ANY) STRICT
# INSERT INTO t1 VALUES('000123')
# SELECT typeof(a), quote(a) FROM t1
# -- result: text '000123'

# ordinary non-strict
# CREATE TABLE t1(a ANY)
# INSERT INTO t1 VALUES('000123')
# SELECT typeof(a), quote(a) FROM t1
# -- result: integer 123
