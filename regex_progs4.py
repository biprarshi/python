import re

a1 = '''Abraham has scored 98 marks
Shakira has scored 95 marks
Tony has scored 875 marks'''
b1 = 'fantastic five turtles'
print(re.findall(r"\d+",a1))
print(re.findall(r'[A-Z][a-z]*',a1))
p1 = re.compile("[a-d]")
print(re.findall(p1,a1))
p1 = re.compile("[0-9]")
print(re.findall(p1,a1))
p1 = re.compile(r"\d+")
print(re.findall(p1,a1))
print(re.split(r"\d+",a1))
print(re.sub(r"\s+","#",a1))
print(re.subn(r"\s+","#",a1))
print(re.escape(a1))
print(re.search(r"\d+",a1))

a2 = "Amit has scored 98 marks"
match1 = re.search(r"\d+", a2)
print(match1)
print(match1.re)
print(match1.string)
print(match1.start())
print(match1.end())
print(match1.span())
print(match1.group())
m1 = re.search(r"\w{2}s", a2)
print(m1)
print(m1.group())

# Number Verification
phn1 = "229-445-8787"
if re.search(r"\d{3}-\d{3}-\d{4}", phn1):
    print("It is a verified No.!!!")
else:
    print("Incorrect No.!!!")

# Email Verification
# email1 = input("Enter email id: ")
email2 = "amit78@gm-a.il.com john@.com raju_989@yahoo.com jon.909@yahoo.com"
# print(re.findall("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email2))
print(re.findall(r"[\w.]{1,20}@[A-Za-z0-9-.]+\.[A-Za-z]{2,}", email2))
