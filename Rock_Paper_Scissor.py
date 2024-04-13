import random

comp_score = 0
user_score = 0
i = "y"
option = ["rock", "paper", "scissor"]

print("-----Rock, Paper, Scissor Game-----")

while (i == "y" or i == "Y"):
        computer = random.choice(option)
        user = input("Enter your choice: ")
        if user == "rock" and computer == "scissor":
            user_score += 1
            print("Computer's choice: ",computer)
            print("You Win!!! Rock beats Scissors :)")
        elif user == "paper" and computer == "rock":
            user_score += 1
            print("Computer's choice: ",computer)
            print("You Win!!! Paper beats Rock :)")
        elif user == "scissor" and computer == "paper":
            user_score += 1
            print("Computer's choice: ",computer)
            print("You Win!!! Scissors beats Paper :)")
        elif user == computer:
             print("Computer's choice: ",computer)
             print("Its an Tie!!!")
        else:
            comp_score += 1
            print("Computer's choice: ",computer)
            print("You Lose!!! " + computer + " beats " + user + " :( ")
        print("Score is: \n Your Score: " + str(user_score) + " Computer Score: " + str(comp_score))
        i = input("Want to play again? Then press 'Y': ")
        continue