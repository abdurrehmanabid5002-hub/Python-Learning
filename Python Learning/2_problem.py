p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe"
p4 = "click"
while True:
    user = input("enter your message :")
    if user.lower() == "exit":
        break

    if (p1 in user or p2 in user or p3 in user or p4 in user):
        print("scam alert!")
    else:
        print("koi msla nai bava ji ")
