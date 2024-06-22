def func1():
    try:
        l = [6,7,8,9,6]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Its an error. Correct it!")
        return 0
    finally:
        print("I am always executed1")
    print("I am always executed2")

x = func1()
print(x)