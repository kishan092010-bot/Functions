try:

    number=int(input("Enter a number: "))

    print("You entered:", 100/number)

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")

except ValueError:

    print("Error: Invalid input. Please enter a valid integer.")

except:

    print("An unexpected error occurred.")

