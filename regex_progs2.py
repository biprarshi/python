# Special Sequences

import re

a = "harry potter"
b = "harrypotter@12345"

match1 = re.search(r"\Ahar",a)
match1 = re.search(r"potter\Z",a)
match1 = re.search(r"\bpo",a)   #Matches if the word begins or end with the given character \b(string),(string)\b
match1 = re.search(r"er\b",a)   #Matches if the word begins or end with the given character \b(string),(string)\b
match1 = re.search(r"ry p\B",a)   #\B it opposite of the \b i.e the string should not start or end with the given regex
match1 = re.search(r"\Bry p",a) 
match1 = re.findall(r"\d",b)
match1 = re.findall(r"\D",b)
match1 = re.findall(r"y\sp",a)
match1 = re.findall(r"\S",b)
match1 = re.findall(r"\w",b)    #Returns a match where the string contains any word characters (characters from A to Z, characters from a to z, digits from 0-9, and the underscore _ character)
match1 = re.findall(r"r\W",b)
print(match1)


