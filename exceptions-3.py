try:
    l = [6,7,8,9,6]
    i =  int(input("Enter the index: "))
    print(l[i])
except:
    print("Its an error. Correct it!")
finally:
    print("I am always executed1")

print("I am always executed2")