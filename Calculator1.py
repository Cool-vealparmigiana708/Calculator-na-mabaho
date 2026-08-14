def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, ** (power), % (modulus)")
    print("Type 'quit' to exit\n")

    while True:
        expression = input("Enter calculation: ")

        if expression.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            parts = expression.split()
            if len(parts) != 3:
                print("Please use format: number operator number\n")
                continue

            num1, operator, num2 = parts
            num1, num2 = float(num1), float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero\n")
                    continue
                result = num1 / num2
            elif operator == '**':
                result = num1 ** num2
            elif operator == '%':
                result = num1 % num2
            else:
                print(f"Unknown operator: {operator}\n")
                continue

            # Show as int if it's a whole number
            if result == int(result):
                result = int(result)
            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid input. Please enter numbers only.\n")


if __name__ == "__main__":
    calculator()