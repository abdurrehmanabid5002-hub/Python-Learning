def countdown(n):
    if n == 0:
        print("Done")
        return

    print(n)
    countdown(n - 1)


countdown(5)



def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]

target = 40

result = binary_search(numbers, target)

if result != -1:
    print("Found at index:", result)
else:
    print("Number not found.")