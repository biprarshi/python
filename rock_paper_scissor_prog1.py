#Rock vs paper ->paper wins
#Rock Vs Scissor-> Rock wins
#paper vs Scissor->Scissor wins

import random
list_for_computer1 = ['Rock', 'Paper', 'Scissors']

while True:
    enter_game1 = int(input(f'''{'':+^25}
Rock Paper Scissors Game
Press 1 to Start Playing
Press 2 to Exit the Game
{'':+^25}
Please Enter Your Choice: '''))

    user_count1 = 0
    computer_count1 = 0

    if enter_game1 == 1:
        for times1 in range(5):
            user_choice1 = int(input(f'''
Press 1 for Rock
Press 2 for Paper
Press 3 for Scissors

Turn {times1+1}, Enter Your Choice: '''))
            if user_choice1 == 1:
                user_got1 = "Rock"
            elif user_choice1 == 2:
                user_got1 = "Paper"
            elif user_choice1 == 3:
                user_got1 = "Scissor"
            else:
                print("Invalid Input")
                times1 -= 1
                continue
            computer_got1 = random.choice(list_for_computer1)
            if computer_got1 == user_got1:
                print("Computer:",computer_got1)
                print("User:",user_got1)
                print("Draw!")
                user_count1 += 1
                computer_count1 += 1
            elif (computer_got1 == "Rock" and user_got1 == "Paper") or (computer_got1 == "Paper" and user_got1 == "Scissors") or (computer_got1 == "Scissors" and user_got1 == "Rock"):
                print("Computer:",computer_got1)
                print("User:",user_got1)
                print("User Wins!")
                user_count1 += 1
            else:
                print("Computer:",computer_got1)
                print("User:",user_got1)
                print("Computer Wins!")
                computer_count1 += 1
        if computer_count1 == user_count1:
            print(f"{'':#^30}\n\nFinal Reesult: Game Draw!!\n")
            print("Computer Score:",computer_count1)
            print("User Score:",user_count1,"\n")
        elif computer_count1 < user_count1:
            print(f"{'':#^30}\n\nFinal Reesult: User Wins!!\n")
            print("Computer Score:",computer_count1)
            print("User Score:",user_count1,"\n")
        else:
            print(f"{'':#^30}\n\nFinal Reesult: Computer Wins!!\n")
            print("Computer Score:",computer_count1)
            print("User Score:",user_count1,"\n")
    elif enter_game1 == 2:
        print("\nBye!")
        break
    else:
        print(f"{'':*^30}\nInvalid Input!! Please Try Again!!")