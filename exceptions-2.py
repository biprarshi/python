try:
    num = int(input("Enter an integer index: "))
    a = [4,5,6,8,9,6]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Value at index not found")
