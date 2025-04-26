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
    username = input("Think of a cool username of at least five characters and enter it here: \n")
    print(f"The entered username is {username}")

start_game()
