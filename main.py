def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}                     #We do not use the () after functions inside the dictionary remember, we are storing the function we are not trigering it!.
type_n = True
while type_n == True:  # outer while loop to start every thing from the very begning.
    print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

    """)
    first_no = float(input("Enter first number: "))

    still_calculating = True
    while still_calculating == True:   # inner while loop to continue calculating with the result.
        operator = input(" + \n - \n * \n / \n Pick an operator:")
        second_no = float(input("Enter second number: "))

        result = operations[operator](first_no, second_no)
        print(f"{first_no} {operator} {second_no} = {result}")

        want_to_continue_with = input("Type 'y' to continue calculating with " + str(result) + " or type 'n' to start a new calculation: ").lower()
        if want_to_continue_with == "y":
            still_calculating = True
            first_no = result
        elif want_to_continue_with == "n":
            still_calculating = False
            print("\n"*100)
            type_n = True
        else:
            print("You did not type 'y' or 'n'")
            still_calculating = False
            print("\n"*100)
            type_n = True

