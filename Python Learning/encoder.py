# ==================Secret Message Encoder==============================

''''text = input("Enter your secret message: ")

encoded = ""

for char in text:
    if char.isalpha():
        encoded += chr(ord(char) + 3)
    else:
        encoded += char

print("🔐 Encoded:", encoded)'''


# Loding effects
''''import time

print("Starting AI system...")

for i in range(20):
    print("█" * i + " " * (20 - i), end="\r")
    time.sleep(0.1)

print("\n🤖 AI System Ready!")'''


# Terminal Matrix Effects
import random
import time

chars = "01"

for _ in range(50):
    line = ""

    for _ in range(80):
        line += random.choice(chars)

    print(line)
    time.sleep(0.05)