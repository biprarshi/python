age = int(input("Please enter your Age: "))
ball = input("Are you a Baller?(y/n) ")
bat = input("Are you a Batsman?(y/n) ")
if age > 16 and ball == "y" or age > 16 and bat == "y":
    print("You are qualified!")
else:
    print("You are disqualified!")
