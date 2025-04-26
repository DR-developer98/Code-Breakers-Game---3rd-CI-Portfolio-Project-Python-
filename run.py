import random
import colorama

def start_game():
    """
    Starts the game, explaining the rules
    """
    print("--------------------------------------")
    print("Welcome to 'THE CODE BREAKERS GAME'!")
    print("Time to flex your logic muscles! Can you crack the code?")
    print("Here's how it works:")
    print("1. A secret code (4 to 10 digits) is generated (with numbers between 0 and 10)")
    print("2. Your job is to guess the code by entering the right number of digits")
    print("3. With each attempt you'll be provided with the following feedback:\n")
    print("O = right digit in the right place")
    print("X = right digit in the wrong place\n")
    print("Use this feedback to adjust your strategy.")
    print("Have fun and happy code breaking!")
    print("--------------------------------------")
    while True:
        try:
            entered_username = input("Choose a username (at least 5 characters): \n")
            if validate_username(entered_username):
                print("The entered username is valid!")
                break
        except ValueError as e:
            print(f"Error: {e}")
    return entered_username

def validate_username(username):
    """
    Checks for right number of digits in username
    """
    if " " in username:
        raise ValueError("The username may not contain blank spaces, use dashes or underscores instead")
    elif len(username) <5:
        raise ValueError(f"The username must contain at least 5 characters, you entered {len(username)}")
    else:
        return True

def choose_mode(username):
    """
    Presents user with a mode-choosing menu.
    """
    print(f"Hi, {username}, how hard will you be challenging yourself today?")
    print("Choose mode:\n")
    print("1. Easy (4-digit code)\n")
    print("2. Medium (6-digit code)\n")
    print("3. Hard (10-digit code)\n")
    while True:
        entered_mode = int(input("Please enter 1, 2 or 3 for the desired mode: \n"))
        try:
            if validate_mode(entered_mode):
                #print("Entered mode is valid!") delete this print statement
                break
        except ValueError as e:
            print(f"Error: {e}")
    return entered_mode
                
def validate_mode(mode):
    if mode not in [1, 2, 3]:
        raise ValueError("Invalid input. Please enter 1, 2 or 3")
    else:
        return True
    
def generate_secret_code(username, mode):
    """
    Generates the secret code to be guessed by the user.
    Uses entered numeric value to generate a secret code 
    with as many digits as dictated by the selected mode.
    """
    print("Generating the secret code...\n")
    secret_code = []
    number_of_digits = None
    if mode == 1:
        for i in range(4):
            x = random.randrange(11)
            secret_code.append(x)
        number_of_digits = 4
    if mode == 2:
        for i in range(6):
            x = random.randrange(11)
            secret_code.append(x)
        number_of_digits = 6
    if mode == 3:
        for i in range(10):
            x = random.randrange(11)
            secret_code.append(x)
        number_of_digits = 10
    print("The secret code has been generated!")
    print("Get your brain fluids flowin' and crack the code!\n")
    while True:
        guessed_code = input(f"Enter your {number_of_digits} digits here, separated by a comma: ")
        try: 
            if validate_guessed_code(guessed_code):
                break
        except ValueError as e:
            print(f"Error: {e}")
    return secret_code
        
chosen_username = start_game()
selected_mode = choose_mode(chosen_username)
generated_code = generate_secret_code(chosen_username, selected_mode)


