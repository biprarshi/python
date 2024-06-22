size = int(input("Enter size: "))

for i in range(size):
    for j in range(size):
        if (i == j) or (i+j == size-1) or (i == size//2) or (j == size//2):
            print("*  ", end='')
        else:
            print("   ", end='')
    print("")

'''
Enter size: 5
*  0 0*  0 1*  0 2*  0 3*  0 4
*  1 0*  1 1*  1 2*  1 3*  1 4
*  2 0*  2 1*  2 2*  2 3*  2 4
*  3 0*  3 1*  3 2*  3 3*  3 4
*  4 0*  4 1*  4 2*  4 3*  4 4
'''

# size = int(input("Enter size: "))
# for i in range(size):
#     for j in range(size):
#         print(i,j,sep=" ", end="    ")
#     print()
