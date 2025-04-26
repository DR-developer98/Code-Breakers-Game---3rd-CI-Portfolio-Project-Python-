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
    print("1. A secret code (4 to 10 digits) is generated")
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
        
start_game()
