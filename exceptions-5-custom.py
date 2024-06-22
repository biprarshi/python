# custom errors(raising custom errors)! Google Python error classes!
class Error1(Exception):
    "custom error"
a = int(input("Enter any value between 5 and 9: "))

try:
    if(a < 5 or a > 9):
        print(a, "1")
        raise Error1("Value should be between 5 and 9")
        print(a, "2")
except Error1 as e:
    print("bah")
    print(e)