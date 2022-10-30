logo = """
 _____________________
|  _________________  |
| | Pythoncalc   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

# addition

def add(n1 , n2):
    return n1 + n2

# subtraction

def subtract(n1 , n2):
    return n1 - n2

# multiply

def multiply(n1 , n2):
    return n1 * n2

# divide

def divide(n1 , n2):
    return n1 / n2

# power

def power(n1 , n2):
    return n1 ** n2


operators = {
    "+":add, 
    "-":subtract, 
    "*":multiply, 
    "/":divide,
    "**": power
}

def start_again():
    
    first_number = float(input("Enter the first number: "))

    for symbol in operators:
        print(symbol)

    wants_to_continue = True
    while wants_to_continue:

        chosen_symbol = input("Which operator/symbol would you like to choose? ")

        second_number = float(input("Enter the next number: "))

        calculation = operators[chosen_symbol]
        answer = calculation(first_number , second_number)

        print(f"{first_number} {chosen_symbol} {second_number} = {answer} ") 

        if input(f" To continue with {answer} press 'y' or press 'n' to start over again: ") == "y":
            first_number = answer
            
        else:
            print(logo)
            wants_to_continue = False
            start_again()
start_again()
    
