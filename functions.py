"""
∘C=(∘F−32)×95​​

"""


def F_TO_C():
    f = int(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"The celcius of {f} Fahrenheit is : {c}")


F_TO_C()


def fictorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fictorial (n- 1)


n = int(input("Enter the number :"))
print(f"The fictorial of  is {fictorial(n)}")


def fect(n):
    if n==1 or n== 0:
        return 1
    return  n * fect (n-1)

print(fect(3))