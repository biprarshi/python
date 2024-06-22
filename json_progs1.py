# JSON:(JavaScript Object Notaion).
# It is mainly used for storing & transferring data between the browser((FrontEnd) and the server(DataBase).
# JSON is text , written with Java Script object notation.
# Python too support JSON With a built-in package called json.
# It can be used in java devlopment,PHP,java-script,.net as well.
# "import json"  is used to import json ..
# Note: JSON is used to send data base  from backend to Application through API(XML,Python,.Net).
# API has the format of data in JSON format.
# JASON is faster than any other formats.
# Example:From One watsapp User ---->(API)-->Server--->(API) ------>Another watsapp user.

# JSON Supports data types like-->1.String 2.number 3.boolean 4.null 5.object 6.Array
# In pyton ,JSON exists as string,For example:
# p='{"name":"NIIT","lang":["Python","Java"]}'

import json

blog1 = {
    "details1": [
        {
            "URL": "training.com",
            "name": "aptech learning",
            "fees": 12000
        },
        {
            "URL": "coursera.org",
            "name": "free learning",
            "Fees": "5000"
        }

    ]
}
# blog1 = 1234
print(blog1)
print(type(blog1))
to_json1 = json.dumps(blog1)
print("dumps dict to json string")
print(to_json1)
print(type(to_json1))
# Note:JSON works as dictionary (key & value pair)

# Converting JSON to Python Object:
# If you have a JSON string,you can parse it by using the json.loads() method.
x1 = '{"cname":"Python","Fees":12000,"Duration":"2Months"}'
# x1 = '[{"cname":"Python","Fees":"12000","Duration":"2Months"}]'
# x1 = to_json1
print(type(x1))

# parse x1
y = json.loads(x1)
print("loads json string to dict")
print(y)
print(type(y))
for a in y:
    print(y[a])

# Writing & Reading JSON File:
# we have to use file handling read & write operations
j_file1 = open("sample.json", "w")
blog2 = json.loads(to_json1)

# json.dump(blog2, j_file1)
# json.dump(y,j_file1)

blog3 = {
    "person": [
        {
            "Name": "Asim",
            "Genger": "Male",
            "Age": 28,
            "Address":
            {
                "City": "Kolkata",
                "State": "West Bangal"
            },
        },
        {
            "Name": "Ria",
            "Genger": "Female",
            "Age": 20,
            "Address":
            {
                "City": "New Delhi",
                "State": "Delhi NCR"
            },
        },
        {
            "Name": "Vajra",
            "Genger": "Male",
            "Age": 25,
            "Address":
            {
                "City": "Udaipur",
                "State": "Rajasthan"
            },
        }

    ]
}
# json.dump(blog3,j_file1)

totat1 = dict(a=blog2, b=y, c=blog3)
json.dump(totat1, j_file1)
# json.dump(12345, j_file1)
print("File Conversion to JSON Successfull")
print("dump dict to json file")
print(j_file1)
j_file1.close()
j_file1 = open("sample.json")
read1 = json.load(j_file1)
print("load json file to dict")
print(read1)
j_file1.close()

# print()
# file1 = open("sample1.json","w")
# json.dump(123,file1)
# file1.close()

# file1 = open("sample1.json")
# load1 = json.load(file1)
# print(load1)

# file1.close()
