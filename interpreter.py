def main():
    # Prompt the user for an arithmetic expression
    expression = input("Expression: ")

    # Check for operators and split accordingly
    if "+" in expression:
        x, z = expression.split("+")
        y = "+"
    elif "-" in expression:
        x, z = expression.split("-")
        y = "-"
    elif "*" in expression:
        x, z = expression.split("*")
        y = "*"
    elif "/" in expression:
        x, z = expression.split("/")
        y = "/"
    else:
        print("Invalid operator")
        return

    # Convert x and z to floats
    x = float(x)
    z = float(z)

    # Perform the arithmetic operation
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    # Print the result as a floating-point value formatted to one decimal place
    print(f"{result:.1f}")

# Call the main function
if __name__ == "__main__":
    main()

