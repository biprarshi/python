# def right_angled_triangle2(n):
#     print(n)
#     if n==0:
#         return
#     else:
#         right_angled_triangle2(n-1)
#         print(n)
#         print("*  "*n)

# right_angled_triangle2(5)

# def recursion1(n):
#     if n==0:
#         return
#     else:
#         print(n)
#         print(recursion1(n-1))
#         print(n)
# recursion1(2)

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
# print("\n\nRecursion Example Results")
# tri_recursion(3)

def recursion2(num):
    if num > 0:
        result = num - recursion2(num - 1)
        print(result)
    else:
        result = 1
    return result


recursion2(6)

size = 5

for i in range(1, size+1):
    for j in range(i):
        print(f'{i,j}', end='', sep='     ')
    print()
for i in range(size):
    for j in range(size):
        print(f'{i,j}', end='', sep='     ')
    print()
