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



import numpy as np

marks = np.array([78, 92, 65, 88, 45, 76, 95, 59, 81, 70])

print("Marks:", marks)

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

print("Passed:", marks[marks >= 50])
print("Failed:", marks[marks < 50])

print("Number of Passed Students:", np.sum(marks >= 50))
print("Number of Failed Students:", np.sum(marks < 50))