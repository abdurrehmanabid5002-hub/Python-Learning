print("=" * 40)
print("          PYTHON CALCULATOR")
print("=" * 40)

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "7":
        print("\nCalculator closed. Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice. Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            symbol = "+"

        elif choice == "2":
            result = num1 - num2
            symbol = "-"

        elif choice == "3":
            result = num1 * num2
            symbol = "*"

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            result = num1 / num2
            symbol = "/"

        elif choice == "5":
            result = num1 ** num2
            symbol = "**"

        elif choice == "6":
            if num2 == 0:
                print("Cannot use zero for modulus.")
                continue
            result = num1 % num2
            symbol = "%"

        print("\n" + "-" * 40)
        print(f"Result: {num1:g} {symbol} {num2:g} = {result:g}")
        print("-" * 40)

    except ValueError:
        print("Please enter valid numbers.")