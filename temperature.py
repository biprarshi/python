print("1. Convert Celsius to Fahrenheit:")
print("2. Convert Fahrenheit to Celsius:")
option=input("Enter your choice(1 or 2): ")
if option=="1":
    temperature=float(input("Enter temperature in Celsius: "))
    result=(temperature*9/5)+32
    print(str(temperature)+"°C in Fahrenheit is "+str(result)+"°F.")
elif option=="2":
    temperature=float(input("Enter temperature in Fahrenheit: "))
    result=(temperature-32)*5/9
    print(str(temperature)+"°F in Celsius is "+str(result)+"°C.")
else:
    print("Invalid input! Please try again!")
