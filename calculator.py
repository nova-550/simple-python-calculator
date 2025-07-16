def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 == 0:
        raise ValueError("Cannot divide by zero.")
    return number1 / number2

def modulus(number1, number2):
    return number1 % number2

while True:
    print("\nSimple Calculator\n")
    
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exit")

    choice = input("\nSelect an operation (1-6): ")
    if choice == '1':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        print(f"Result: {addition(num1, num2)}")

    elif choice == '2':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        print(f"Result: {subtraction(num1, num2)}")
    
    elif choice == '3':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        print(f"Result: {multiplication(num1, num2)}")

    elif choice == '4':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        try:
            print(f"Result: {division(num1, num2)}")
        except ValueError as e:
            print(e)

    elif choice == '5':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        print(f"Result: {modulus(num1, num2)}")

    elif choice == '6':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid operation (1-6).")

