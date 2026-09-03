board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_board():
    for row in board:
        print(" ".join(str(x) if x != 0 else "." for x in row))


def find_empty():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def valid(number, row, col):
    for i in range(9):
        if board[row][i] == number:
            return False

    for i in range(9):
        if board[i][col] == number:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == number:
                return False

    return True


def solve():
    empty = find_empty()

    if empty is None:
        return True

    row, col = empty

    for number in range(1, 10):
        if valid(number, row, col):
            board[row][col] = number

            if solve():
                return True

            board[row][col] = 0

    return False


print("Original Sudoku:\n")
print_board()

if solve():
    print("\nSolved Sudoku:\n")
    print_board()
else:
    print("No solution exists.")




from collections import Counter

words = [
    "python",
    "program",
    "computer",
    "science",
    "developer",
    "data",
    "analysis",
    "machine",
    "learning",
    "algorithm",
    "function",
    "variable"
]

letters = input("Enter letters: ").lower()

available = Counter(letters)

matches = []

for word in words:
    required = Counter(word)

    if required <= available:
        matches.append(word)

print("\nPossible words:")

for word in matches:
    print(word)



import random
import time

number = random.randint(10000, 99999)

print("Remember this number:")
print(number)

time.sleep(3)

print("\n" * 30)

answer = input("What was the number? ")

if answer == str(number):
    print("Correct.")
else:
    print("Wrong.")
    print("The number was:", number)
    