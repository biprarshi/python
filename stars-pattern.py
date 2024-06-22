size = int(input("Enter size: "))
# star
for i in range(size):
    for j in range(size):
        if (i==j) or (i+j==size-1) or (i==size//2) or (j==size//2):
            print("*  ", end='')
        else:
            print("   ", end='')
    print("")
# square
for i in range(size):
    print("*  "*size)
# hollow sqare
for i in range(size):
    for j in range(size):
        if (i==0) or (i==size-1) or (j==0) or (j==size-1):
            print("*  ", end='')
        else:
            print("   ", end='')
    print("")

def right_angled_triangle(n):
    triangle_list = ["*"]
    for i in range(n-1):
        triangle_list.append("*  "*(i+2))
    print("\n".join(triangle_list))
right_angled_triangle(size)

def right_angled_triangle2(n):
    if n==0:
        return
    else:
        right_angled_triangle2(n-1)
        print("*  "*n)        
right_angled_triangle2(size)

# def right2(n):
#     k = 2*n-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end='')
#         k = k-2
#         for j in range(0,i+1):
#             print('*  ',end='')
#         print('\r')
# right2(size)

# for i in range(1,size+1):
#     for j in range(i):
#         if j==0 or j==i-1:
#             print('* ',end='')
#         else:
#             if i!=size:
#                 print('   ',end='')
#             else:
#                 print('*  ',end='')
#     print()                

for i in range(size):
    for j in range(i):
        if j==0 or j==i-1:
            print('*  ',end='')
        else:
            print('   ',end='')

    print("")
print('*  '*size)                

for i in range(size,0,-1):
    for j in range(0,i):
        print('*  ',end='')
    print()

def alphabet_1(n):
    num = 65
    for i in range(n):
        for j in range(i+1):
            ch = chr(num)
            print(ch,end='')
        num = num+1
        print('\r')
alphabet_1(size)

def contnum_1(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num,end='')
            num = num+1
        print('\r')
contnum_1(size)

# Reverse Right

# def pypart2(n):

# 	k = 2*n - 2

# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
			
# 		k = k - 2
# 		for j in range(0, i+1):
# 			print("* ", end="")
# 		print("\r")
# n = 8
# pypart2(n)

for i in range(size):
    for j in range(size):
        if i+j < (size//2)+3:
            print('  ', end='')
        else:
            print('* ', end='')
    print('')
    
for i in range(size):
    print('  '*(size-i-1)+'* '*(i+1))

# equilateral
# def triangle(n):

# 	k = n - 1
# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
# 		k = k - 1
# 		for j in range(0, i+1):
# 			print("* ", end="")
# 		print("\r")
# n = 5
# triangle(n)
for i in range(size):
    print('  '*((size-i-1))+'*   '*(i+1))

# inverse Equilateral
# num_rows = int(input("Please enter the number of rows"));
# for i in range(num_rows,0,-1):
#     for j in range(0, num_rows-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("* ", end=" ")
#     print()
for i in range(size,0,-1):
    print('  '*(size-i)+'*   '*(i))

# Pyramid
# for i in range (0, size):
#     for j in range(0, i + 1):
#         print("* ", end='')
#     print("\r")
# for i in range (size, 0, -1):
#     for j in range(0, i -1):
#         print("* ", end='')
#     print("\r")
for i in range(size):
    print('* '*(i+1))
for i in range(size-1,0,-1):
    print('* '*i)
