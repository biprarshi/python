# Metacharacters

import re

a = "charlie chaplin coa  chaaaaaaa   and Baaaaa Baaaaaa black sheep"
b = "niit123@gmail.com"
c = "Hello"
d = "xyz,yz,xyyyz,xyzz,xyyz,xxzzy,zyyyyz,xxyyyzz"

match1 = re.search(r"\.",b)     #Signals a special sequence (can also be used to escape special characters)
match1 = re.search(r"[@]",b)    #[]	A set of characters
match1 = re.findall(r"[l]",c)
match1 = re.search(r"^B",c)     #Starts with	
match1 = re.search(r"com$",b)   #Ends with
match1 = re.findall(r"c.a",a)   #Any character (except newline character) 
match1 = re.findall(r"cha|Ba",a)    #Either or
match1 = re.search(r"cha|Ba",a) #Either or
match1 = re.findall(r"a?",a)   #Zero or one occurrences
match1 = re.findall(r"a?a",a)
match1 = re.findall(r"a*a",a)   #Zero or more occurrences
match1 = re.findall(r"xy+z",d)  #One or more occurrences
match1 = re.findall(r"y{2,4}",d)    #Exactly the specified number of occurrences, number of repeatation between 2 to 4
match1 = re.findall(r"(x|y)yz",d)   #Capture and group
print(match1)
