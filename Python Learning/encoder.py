# ==================Secret Message Encoder==============================

''''text = input("Enter your secret message: ")

encoded = ""

for char in text:
    if char.isalpha():
        encoded += chr(ord(char) + 3)
    else:
        encoded += char

print("🔐 Encoded:", encoded)'''

import time

print("Starting AI system...")

for i in range(20):
    print("█" * i + " " * (20 - i), end="\r")
    time.sleep(0.1)

print("\n🤖 AI System Ready!")