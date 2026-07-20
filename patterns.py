# i = 1
# while True:
#     n = int(input("enter a number : "))
#     if n == 0:
#         break
#     else:
#         for i in range(1, n + 1):
#             print(" " * (n - i), end="")
#             print("*" * (2 * i - 1))
#             # print("")


# i = 1
# while True:
#     n = int(input("enter a number : "))
#     if n == 0:
#         break
#     for i in range(1, n+1):
#         if i == 1 or i == n:
#             print("*" * n, end="")
#         else:
#             print("*", end="")
#             print(" " * (n - 2), end="")
#             print("*", end="")
#         print("")


i = 1
while True:
    n = int(input("enter a number : "))
    if n == 0:
        break
    for i in range (1,11 ):
        print (f"{n}x{i}={n*i}")