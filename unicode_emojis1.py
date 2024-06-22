a1 = []
a2 = []

# length = 201513
# length = 1114078
# length = range(160, 9951)
# length = range(9952, 127775)
# #length = range(127776, 128255)
# length = range(128256, 129007)
# length = range(129008, 129791)
# length = range(9728, 9983)

# length = range(58)
# for i in length:
#     if i >25 and i <32:
#         pass
#     else:       
#         print(i) 
#         a1.append(i+1)
#         a2.append(chr(i+65))

# length = range(10)
# for i in length:
#     a1.append(i+1)
#     a2.append(0-(i+1))

# length = range(127776, 128256)
# for i in length:
#     a1.append(i)
#     a2.append(chr(i))

length = range(9728, 9984)
for i in length:
    a1.append(i)
    a2.append(chr(i))


bb = []

for i in range(len(a1)):
    bb.append((a1[i],a2[i]))

print(bb)
