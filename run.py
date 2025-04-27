import random

def start_game():
    """
    Starts the game, explaining the rules
    """
    print("--------------------------------------")
    print("--------------------------------------")
    print("Welcome to 'THE CODE BREAKERS GAME'!")
    print("Time to flex your logic muscles! Can you crack the code?")
    print("Here's how it works:")
    print("1. A secret code (4 to 10 digits) is generated (with numbers between 0 and 10)")
    print("2. Your job is to guess the code by entering the right number of digits")
    print("3. With each attempt you'll be provided with the following feedback:\n")
    print("O = right digit in the right place")
    print("X = right digit in the wrong place")
    print("- = wrong digit (not an element of the secret code)\n")
    print("Use this feedback to adjust your strategy.")
    print("Have fun and happy code breaking!")
    print("--------------------------------------")
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
                break
        except ValueError as e:
            print(f"Error: {e}")
    return entered_mode
                
def validate_mode(mode):
    """
    Checks for correct mode input.
    Raises an error when the input isn't 1, 2 or 3.
    """
    if mode not in [1, 2, 3]:
        raise ValueError("Invalid input. Please enter 1, 2 or 3")
    else:
        return True
    
def generate_secret_code(mode):
    """
    Generates the secret code to be guessed by the user.
    Uses entered numeric value to generate a secret code 
    with as many digits as dictated by the selected mode.
    """
    print("Generating the secret code...\n")
    secret_code = []
    number_of_digits = None
    number_of_attempts = None
    if mode == 1:
        for i in range(4):
            x = random.randrange(11)
            secret_code.append(x)
        number_of_digits = 4
        number_of_attempts = 4
    elif mode == 2:
        for i in range(6):
            x = random.randrange(11)
            secret_code.append(x)
        number_of_digits = 6
        number_of_attempts = 6
    elif mode == 3:
        for i in range(10):
            x = random.randrange(11)
            secret_code.append(x)
        number_of_digits = 10
        number_of_attempts = 10
    print("The secret code has been generated!\n")
    print("Get your brain juices flowin' and start crackin' the code!\n")
    print(f"The number of digits is: {number_of_digits}")
    print(f"DELETE; the secret code is{secret_code}")#DELETE!!!
    return (secret_code, number_of_digits, number_of_attempts)

def validate_guessed_code(user_code, digits):
    """
    Performs a check on the entered code.
    Raises an error:
    1) if the number of digits isn't the correct one;
    2) if the guessed code contains numbers 
    not included in the range 0-10;
    3) if the user inputs a non-numeric value in the code.
    """
    for x in user_code:
        if x not in range(11):
            raise ValueError("The code may only contain numbers between 0 and 10")
    #Add condition to check for non-numerical characters in the entered code
    if len(user_code) != digits:
        raise ValueError(f"In this mode you need to provide {digits} digits, you've only entered {len(user_code)}")
    else:
        return True

def check_guessed_code_against_secret_one(gen_code, attempts, digits):
    """
    Checks the code guessed by the user
    against the secret one and provides feedback.
    """
    print(f"You have a maximum of {attempts} attempts")

    while attempts > 0:
        entered_code = input(f"Enter your {digits} digits here, separated by a comma: \n").split(",")
        guessed_code = [int(x) for x in entered_code]

        try: 
            if validate_guessed_code(guessed_code, digits):
                print("The number of digits is correct!\n")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        feedback = []

        for x, y in zip(guessed_code, gen_code):
            if x in gen_code:
                if x == y:
                    feedback.append("O")
                else:
                    feedback.append("X")
            else:
                feedback.append("-")
    
        attempts -= 1
        if guessed_code == gen_code:
            print("Congratulations! You've cracked the code!")
            break                  
        else:
            print(f"Here is your feedback: {feedback}\n")
            print(f"You have {attempts} attempts left\n")
    if guessed_code != gen_code and attemtps == 0:
        print("Unfortunately, you're out of attempts :(.")
        print("Don't worry, though! You'll get the hang of it ;)")
    return (feedback, attempts, gen_code, digits)

chosen_username = start_game()
selected_mode = choose_mode(chosen_username)
generated_code = generate_secret_code(selected_mode)
feedback = check_guessed_code_against_secret_one(*generated_code)
