import os
from shutil import copyfile
f = open('/home/tomato/Desktop/python/ABC.txt', 'w')        # file is opened
f.write("hello, my name is spidy")        # will write this file.
# only 1 string is allowed in write function

tasks = ['gym ', 'chapter3 ', 'water plants ', 'dogs walk']
f.writelines(tasks)  # will write all strings in the file.

tasks = ['My  ', 'Name  ', 'Is ', 'Groot']
f.writelines(tasks)

f.close()


# append mode
file1 = open("/home/tomato/Desktop/python/ABC.txt", "a")

# writing newline character
file1.write("\n")
file1.write("Today\n")

# without newline character
file1.write("Tomorrow"*10+'\n')
file1.write('Dragon'*5+'\n')
for _ in range(7):
    file1.write('small\n')
print("File Written Successfully..")
file1.close()

f = open("/home/tomato/Desktop/python/ABC.txt")  # File open
# result=f.read()     #read enire file
# print(result,end='EOF')

result = f.readline()      # read only one line
print(result, end='')           # gives all bytes at a time
result = f.readline()
print(result, end='')

print(f.readline(11), end='')  # read 11 characters
print(' '*3, end=' ')
print(f.readline(), end='')  # will print the reaminings.
print(f.readline(), end='')

result = f.readlines()        # gives in list form element
print(result)
f.close()


# readline() does add '\n at the end of every string in the output

f = open("/home/tomato/Desktop/python/ABC.txt", 'a')        # file is opened
f.write(" \nSpidy is Hero")


# # copy file:-

copyfile("/home/tomato/Desktop/python/ABC.txt",
         "/home/tomato/Desktop/python/DELL.txt")

# # or

# sFile = input("Enter the Name of Source File: ")
# dFile = input("Enter the Name of Target File: ")

# fileHandle1 = open(sFile, "r")
# texts1 = fileHandle1.read()
# fileHandle1.close()

# fileHandle2 = open(dFile, "w")
# fileHandle2.write(texts1)
# fileHandle2.close()

print("\nFile Copied Successfully!")

file1 = open("/home/tomato/Desktop/python/DELL.txt")
print(file1.tell())
content1 = file1.read()
print(content1, end="EOF")
content2 = file1.readlines()
print(content1, end="EOF")
print(file1.tell())
file1.seek(0)
content3 = file1.readline()
print(file1.tell())
print(content3, end="EOF")
file1.close()

# importing os module

# Directory
directory1 = "PUBG"

# Parent Directory path
parent_dir1 = "/home/tomato/Desktop/python/"

# Path
path1 = os.path.join(parent_dir1, directory1)
print(path1)

# Create the directory
# os.makedirs(path1)
print("Directory '% s' created" % directory1)
print(f"Directory {directory1} created")


# Delete a file :

# file = 'DELL.txt'
# # File location
# location = "/home/tomato/Desktop/python/"
# path = os.path.join(location, file)
# os.remove(path)

# # or

# os.remove("/home/tomato/Desktop/python/DELL.txt")


# Folder:


# directory = "PUBG"
# # Parent Directory
# parent = "/home/tomato/Desktop/python/"
# # Path
# path = os.path.join(parent, directory)
# # Remove the Directory
# # os.rmdir(path)

# # or

# os.rmdir("/home/tomato/Desktop/python/PUBG")

f1 = open("1.py (copy)", "rb")
# print(f1.read())
f1.seek(-2, 2)
# f1.seek(5, 0)
print(f1.tell())
print(f1.read())
f1.close()
'''In Python, seek() function is used to change the position of the File Handle to a given specific position. File handle is like a cursor, which defines from where the data has to be read or written in the file. 
 

Syntax: f.seek(offset, from_what), where f is file pointer
Parameters: 
Offset: Number of positions to move forward 
from_what: It defines point of reference.
Returns: Return the new absolute position.

The reference point is selected by the from_what argument. It accepts three values: 
 

0: sets the reference point at the beginning of the file 
 
1: sets the reference point at the current file position 
 
2: sets the reference point at the end of the file 
 
By default from_what argument is set to 0.
Note: if file not opened in rb mode "from_what"=2 cannot be used with -ve offset.'''
