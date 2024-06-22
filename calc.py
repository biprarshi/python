import sys

operator=input("Enter Oprator: ")

try:
    operand1=float(input("Enter Operand1: "))
except:
    sys.exit("Invalid Input! Please try again!!")

operand2=""
while type(operand2)!= float:
    try:
        operand2=float(input("Enter Operand2: "))
    except:
        continue
    
if operator=="+" :
    result=operand1+operand2
elif operator=="-" :
    result=operand1-operand2
elif operator=="*" :
    result=operand1*operand2    
elif  operator=="/" :
    result=operand1/operand2
elif  operator=="//" :
    result=operand1//operand2
elif  operator=="**" :
    result=operand1**operand2
elif  operator=="%" :
    result=operand1%operand2
else :
    print("Invalid Operator! Please Try Again!!")
    sys.exit()
    
print("The result is: "+str(result))
