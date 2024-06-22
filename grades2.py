serial=int(input("Enter serial No:(1-200) "))
if serial>0 and serial<51 :
    print("You belong to Grade A!")
elif serial>50 and serial<101 :
    print("You belong to Grade B!")
elif serial>100 and serial<151 :
    print("You belong to Grade C!")
elif serial>150 and serial<201 :
    print("You belong to Grade D!")
else :
    print("Exception!")
