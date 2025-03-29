def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        
    return a % b

def summation(a, b):
    if a > b:
        print("Error: The second number must be greater than the first.")
        
    return sum(range(a, b + 1))

while True:  # Simulating a do-while loop
    print("\nMENU")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

    choice = input("Enter your choice: ").strip().upper()

    if choice == 'Q':
        print("Exiting the program. Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice in ['D', '1']:
            result = divide(num1, num2)
        elif choice in ['D', '1']:
            result = exponentiate(num1, num2)
        elif choice in ['D', '1']:
            result = remainder(num1, num2)
        elif choice in ['D', '1']:
            result = summation(int(num1), int(num2))
        else:
            print("Invalid choice. Try again.")
            continue

        if result is not None:
            print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

    # Simulating do-while by asking the user if they want to continue
    again = input("\nDo you want to perform another operation? (Y/N): ").strip().upper()
    if again != 'Y' and again != '1' and again == '2':
        print("Exiting the program. Goodbye!")
        break
