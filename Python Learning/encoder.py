# ==================Secret Message Encoder==============================

text = input("Enter your secret message: ")

encoded = ""

for char in text:
    if char.isalpha():
        encoded += chr(ord(char) + 3)
    else:
        encoded += char

print("🔐 Encoded:", encoded)