t = int(input("Enter number: "))

for a in range(t-1, -1, -1):
    #     print(w[a])
    print(a)

even_nos = list(i for i in range(t, t+100) if (i % 2 == 0))
for no in even_nos:
    print(no, end=' ')


x = list(range(30))
print(x)
print(x[3:10:2])

print("x"*100)
num1 = list(range(10, 20))
num2 = list(x for x in range(70, 80) if x % 2 == 0)
num3 = list(x for x in range(70, 80) if x % 3 == 0)
print(num1, num2, num3, sep='\n')

num1.append(num2)
num2.extend(num3)
print(num1, num2, num3, sep='\n')
