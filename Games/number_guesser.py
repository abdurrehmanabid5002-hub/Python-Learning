import random

n = random.randint(1, 101)
guesses = 1
a = -1
while a != n:
    with open("Games/number.txt", "r") as f:
        score = f.read()
        if score == "":
            a = int(input("enter the number :"))
            if a > n:
                print("Lower number plzz")
            else:
                print("Higher number plzz")
                guesses += 1


print(f"you guess the number {n} in {guesses} attempts")

with open("Games/number.txt", "w") as f:
    f.write(str(n))
