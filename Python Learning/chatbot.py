import wikipedia

while True:
    user = input("Ask: ")
    if user.lower() == "exit":
        break
    result = wikipedia.search(user)
    if len(result) > 0:
        data = wikipedia.summary(result[0], sentences=2)
        print(data)
    else:
        print("no data found!")
