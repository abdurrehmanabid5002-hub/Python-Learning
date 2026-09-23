import random

print("🪙 Coin Toss Game")

while True:
    choice = input("Choose Heads or Tails: ").lower()

    if choice != "heads" and choice != "tails":
        print("Please choose Heads or Tails.")
        continue

    coin = random.choice(["heads", "tails"])

    print("Coin:", coin)

    if choice == coin:
        print("🎉 You Win!")
    else:
        print("❌ You Lose!")

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break