"""
1 for snake
-1 for water
0 for gun
"""

import random

youstr = input("Enter a number :")
computer = random.choice([-1, 0, 1])
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}
you = youdict[youstr]
print(f"you chose {reversedict[you]  }\nComputer chose {reversedict[you ]}")
if computer == you:
    print("you draw!")
else:
    if computer == -1 and you == 1:
        print("you win!")
    elif computer == -1 and you == 0:
        print("you win!")
    elif computer == 1 and you == -1:
        print("you lose!")
    elif computer == 1 and you == 0:
        print("you win!")
    elif computer == 0 and you == 1:
        print("you lose!")
    elif computer == 0 and you == -1:
        print("you lose!")
    else:
        print("something went wrong !")
