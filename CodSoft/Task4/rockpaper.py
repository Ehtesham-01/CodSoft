# Rock, Paper , Scissor Game
import random
string=["Rock","Paper","Scissor"]
print("Choose any one of them ('Rock',Paper','Scissor')")
your_choice=input("Enter your choice= ").strip().capitalize()
computer_choice = random.choice(string)
if your_choice in string:
    if your_choice == computer_choice:
        print("Tied..")
        print("Your choice is= ",your_choice)
        print("Your computer choice is= ",computer_choice)
    elif your_choice == "Rock" and computer_choice == "Scissor":
        print("You Win..")
        print("Your choice is= ",your_choice)
        print("computer choice is= ",computer_choice)
    elif your_choice == "Scissor" and computer_choice == "Paper":
        print("You Win..")
        print("Your choice is= ",your_choice)
        print("Your computer choice is= ",computer_choice)
    elif your_choice == "Paper" and computer_choice == "Rock":
        print("You Win..")
        print("Your choice is= ",your_choice)
        print("Your computer choice is= ",computer_choice)
    else:
        print("You Lose..")
        print("Your choice is= ",your_choice)
        print("Your computer choice is= ",computer_choice)
else:
    print("Invalid choose. please enter valid choice.")