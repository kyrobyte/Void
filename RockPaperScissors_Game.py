# Import Statements:

import random

# Rock Paper Scissors Game:

print("Winning rules of rock, paper, scissors game are as follows:\n"
      + "Rocks vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissors win\n")

while True:
    print("\n Enter choices\n 1 for Rock, 2 for Paper, and 3 for scissor.\n")
    choice = int(input("User's Turn "))  # Input
    while choice > 3 or choice < 1:
        choice = int(input("Enter Valid Input "))  # If choice is not valid
    if choice == 1:  # If Rock
        choice_name = 'Rock'
    elif choice == 2:  # If Paper
        choice_name = 'Paper'
    else:  # If Scissor
        choice_name = 'Scissor'
    print("The user's choice is: " + choice_name)

    print("\n Now its the computer's turn...")  # Computer's Turn
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        compname = 'Rock'
    elif comp_choice == 2:
        compname = 'Paper'
    else:
        compname = 'Scissor'

    print("Computer choice is: " + compname)

    print(choice_name + " vs " + compname)

# Conditions for the Game:

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("Paper wins -> ", end="")
        result = "Paper"

    if ((choice == 2 and comp_choice == 3) or
            (choice == 3 and comp_choice == 2)):
        print("Scissor Wins -> ", end="")
        result = "Scissor"

    if ((choice == 1 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)):
        print("Rock Wins ->", end="")
        result = "Rock"
