import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Choose rock, paper or scissors: ").lower()

print("Computer:", computer)

if player == computer:
    print("Draw!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

else:
    print("Computer wins!")