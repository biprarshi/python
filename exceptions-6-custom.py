class InvalidAgeException(Exception):
    "Raised when input value is less than 18"



number = 18
try:
    input_num = int(input("Enter your age: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to vote!")
except InvalidAgeException:
    print("Exception Occured: Invalid Age")
except ValueError:
    print("Invalid Input")