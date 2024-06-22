from time import sleep

time1 = eval(input("Enter time: "))

i = 0

while i < time1:
    print(i + 1)
    i = i + 1
    sleep(1 if i < time1 else 0)