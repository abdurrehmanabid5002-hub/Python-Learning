# print("Helo World "
name = input("enter your name : ")
print("your name in :",name )
letter = "I am a good boy"
print (letter.replace ("good", "bad"))
print (letter)
a= int (input("enter a number : " ))


b= int (input("enter a number : " ))
print ( a*b)


letter = "i am a good boy and ali in not a good boy "
print (letter.capitalize().replace("good", "bad").replace("ali", "ahmad"))
print(letter)
greet()

s = set()
for i in range(5):
    n = input("Enter the number :")
    s.add(int(n))

print("The unique numbers are : ", s)


d = {}
for i in range(7):
    lang = input("Enter the language : ")
    person = input("Enter the person name : ")
    d.update({lang: person})

print(d)


def greet(name):
    print("Hello", name)
    if name == "Ali":
        print("Welcome")
    else:
        print("Hi")

