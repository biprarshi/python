# Sets

import re

a="charlie and chocholate xfactory"
b="jon#123@34$645"
c="12hi34john^67HELLO73r89"

match1 = re.findall('[atx]',a)
match1 = re.findall('[^atx]',a)  #anything except a t x
match1 = re.findall('^[j]',b)   #prints j
match1 = re.findall('[a-t]',a)
match1 = re.findall('[1234]',b)
match1 = re.findall('[0-5]',b)
match1 = re.findall('[0-7][0-9]',c)
match1 = re.findall('[A-Za-z]',c)
match1 = re.findall('[@$#]',b)
print(match1)