
'''
# lamda 
square =lambda x:x*x
print (square(3))
me = input
# walarus operator 
if name := str(input("Enter your name :")):
    print ( f"Hello there {name}")

numbers =[2,2,4,6,78,3]
if (count:=len(numbers)<2):
    print ( numbers)
else:
    print(count)
try:
    a= int(input("Enter the number :"))
    print (a)
except ValueError as e :
    print ("ValueError")

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")


def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()

l=[2,4,56,7,8,6]
for index , itmes in enumerate(l):
    print  (f"The index {index}: {itmes}")
'''

list=[1,2,3,4,5,6,7,8,9]
squarelist=[i*i for i in list]
print (squarelist)