# # Synatx Errors:Cant be handeled you have to fix the syntax:
# a=10
# b=20

# if a==b 
# 	print("No")
# else
# 	print('yes')

# Logical error:

# print(1/0) 			# Zero Division Error: Division by zero

# l=[10,20,30,40]			#index out of range error
# print(l[6])



# a=int(input("Enter a number"))
# print(a)

a = input("Enter a number: ")
print("Multiplication Table of {} is:".format(a))

# for i in range(1,11):
#     print(f"{int(a)}X{i}={int(a)*i}")

# print("Some imp lines of code")
# print("End")

try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")
except Exception as e:
    print(e)
    print("Sorry this input is not a valid input in table")
print("Some inmportant lines of code")
print("End")

