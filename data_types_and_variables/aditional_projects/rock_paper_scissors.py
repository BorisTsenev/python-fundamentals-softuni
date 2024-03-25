import random

game_choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(game_choices)
is_win = False
print("Welcome to the game of rock, paper, scissors!")
print("You are playing against a machine!")
print("You can choose between rock/paper/scissors, are you ready?")
your_choice = input("Choose your character: ")

if computer_choice == "rock":
    if your_choice == "rock":
        is_win = -1
    elif your_choice == "paper":
        is_win = True
    else:
        is_win = False

elif computer_choice == "paper":
    if your_choice == "paper":
        is_win = -1
    elif your_choice == "scissors":
        is_win = True
    else:
        is_win = False
else:
    if your_choice == "scissors":
        is_win = -1
    elif your_choice == "rock":
        is_win = True
    else:
        is_win = False

if is_win == -1:
    print(f"You are draw!\nYou can`t beat ")