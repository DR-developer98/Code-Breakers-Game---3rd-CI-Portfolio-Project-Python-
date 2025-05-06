import random
from colorama import Fore, Style, init

# ↓↓↓CREDIT: Love Sandwiches Walkthrough Project↓↓↓
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Leaderboard_code_breakers_game")
# ↑↑↑CREDIT: Love Sandwiches Walkthrough Project↑↑↑

init()  # initializes colorama


def start_program():
    """
    Starts the program, explaining the rules
    """
    print("--------------------------------------")
    print("--------------------------------------")
    print("Welcome to 'THE CODE BREAKERS GAME'!")
    print("Time to flex your logic muscles! Can you crack the code?")
    print("Here's how it works:")
    print("1. A secret code (4 to 10 digits) is generated \
(with numbers from 0 to 10 inclusive)")
    print("2. Your job is to guess the code \
by entering the right number of digits")
    print("3. With each attempt you'll be provided \
with the following feedback:\n")
    print(f"{Fore.GREEN + "O" + Style.RESET_ALL} \
= right digit in the right place")
    print(f"{Fore.YELLOW + "X" + Style.RESET_ALL} \
= right digit in the wrong place")
    print(f"{Fore.RED + "-" + Style.RESET_ALL} \
= wrong digit (not an element of the secret code)\n")
    print("Use this feedback to adjust your strategy.")
    print("Have fun and happy code breaking!")
    print("--------------------------------------")
    print("--------------------------------------")
    while True:
        try:
            entered_username = input("Choose a username \
(at least 5 characters): \n")
            if validate_username(entered_username):
                print("The entered username is valid!\n")
                break
        except ValueError as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    return entered_username


def validate_username(username):
    """
    Checks for right number of digits in username
    """
    if " " in username:
        raise ValueError("The username may not contain blank spaces, \
use dashes or underscores instead")
    elif len(username) < 5:
        raise ValueError(f"The username must contain at least 5 characters,\
you entered {len(username)}")
    else:
        return True


def start_rankings_quit(username):
    """
    Presents the user with the possibility to either \
    start playing the game or to view the rankings \
    for the different modes
    """
    print(f"{username}, what would you like to do?\n")
    print("1. Start the game")
    print("2. View rankings")
    print("3. Quit the game\n")
    start_menu_choice_int = None
    while True:
        start_menu_choice = input("Please enter 1, 2 or 3  \
to make a choice:")
        if not start_menu_choice.strip().isdigit():
            print(f"{Fore.RED}Error: \
Invalid input. Please enter 1, 2 or 3{Style.RESET_ALL}")
        else:
            start_menu_choice_int = int(start_menu_choice)
            try:
                if validate_start_menu_choice(start_menu_choice_int):
                    break
            except ValueError as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    return start_menu_choice_int


def validate_start_menu_choice(start_menu_choice_int):
    """
    Checks for correct menu choice input.
    Raises an error when the input isn't 1 or 2.
    """
    if start_menu_choice_int not in [1, 2, 3]:
        raise ValueError("Invalid input. Please enter 1, 2 or 3")
    else:
        return True


def view_rankings():
    """
    Allows the user to view the first 10 \
    items in the rankings for the different modes
    """
    easy_mode = SHEET.worksheet("Easy mode")
    easy_usernames = easy_mode.col_values(1)[1:11]
    easy_scores = easy_mode.col_values(2)[1:11]
    # ↓↓↓CREDIT: stackoverflow↓↓↓
    sorted_easy = sorted(
        zip(easy_usernames, easy_scores),
        key=lambda pair: int(pair[1]), reverse=True)
    # ↑↑↑CREDIT: stackoverflow↑↑↑

    medium_mode = SHEET.worksheet("Medium mode")
    medium_usernames = medium_mode.col_values(1)[1:11]
    medium_scores = medium_mode.col_values(2)[1:11]
    sorted_medium = sorted(
        zip(medium_usernames, medium_scores),
        key=lambda pair: int(pair[1]), reverse=True)

    hard_mode = SHEET.worksheet("Hard mode")
    hard_usernames = hard_mode.col_values(1)[1:11]
    hard_scores = hard_mode.col_values(2)[1:11]
    sorted_hard = sorted(
        zip(hard_usernames, hard_scores),
        key=lambda pair: int(pair[1]), reverse=True)

    print("----------")
    print("----------")
    print(f"{Fore.GREEN + "Easy mode" + Style.RESET_ALL}\n")
    for username, score in sorted_easy:
        print(f"{username}: {score}")
    print("----------")
    print("----------")
    print(f"{Fore.GREEN + "Medium mode" + Style.RESET_ALL}\n")
    for username, score in sorted_medium:
        print(f"{username}: {score}")
    print("----------")
    print("----------")
    print(f"{Fore.GREEN + "Hard mode" + Style.RESET_ALL}\n")
    for username, score in sorted_hard:
        print(f"{username}: {score}")
    print("----------")
    print("----------")


def choose_mode(username):
    """
    Presents user with a mode-choosing menu.
    """
    print(f"Hi, {username}, how hard will you be challenging yourself today?")
    print("Choose mode:\n")
    print("1. Easy (4-digit code)")
    print("2. Medium (6-digit code)")
    print("3. Hard (10-digit code)\n")
    entered_mode_int = None
    while True:
        entered_mode = input("Please enter 1, 2 or 3 \
for the desired mode: \n")
        if not entered_mode.strip().isdigit():
            print(f"{Fore.RED}Error: \
Invalid input. Please enter 1, 2 or 3{Style.RESET_ALL}")
        else:
            entered_mode_int = int(entered_mode)
            try:
                if validate_mode(entered_mode_int):
                    break
            except ValueError as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    return entered_mode_int


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
    Generates the secret code to be guessed by the user. \
    Uses entered numeric value to generate a secret code \
    with as many digits as dictated by the selected mode.
    """
    print("Generating the secret code...\n")
    number_of_digits = None
    number_of_attempts = None
    if mode == 1:
        number_of_digits = 4
        number_of_attempts = 4
    elif mode == 2:
        number_of_digits = 6
        number_of_attempts = 6
    elif mode == 3:
        number_of_digits = 10
        number_of_attempts = 10

    # ↓↓↓CREDIT: geeksforgeeks↓↓↓
    secret_code = random.sample(range(11), number_of_digits)
    # ↑↑↑CREDIT: geeksforgeeks↑↑↑

    print("The secret code has been generated!\n")
    print("Get your brain juices flowin' and start crackin' the code!\n")
    print(f"Your code must contain {number_of_digits} digits")  # DELETE!!!
    print(f"DELETE; the secret code is {secret_code}")  # DELETE!!!
    return (secret_code, number_of_digits, number_of_attempts)


def validate_guessed_code(user_code, digits):
    """
    Performs a check on the entered code.
    Raises an error: \
    1) if the number of digits isn't the correct one; \
    2) if the guessed code contains numbers \
    not included in the range 0-10; \
    3) if the user inputs a non-numeric value in the code.
    """
    for x in user_code:
        if x not in range(11):
            raise ValueError("The code may only contain \
numbers between 0 and 10")
    if len(user_code) != digits:
        raise ValueError(f"In this mode you need to provide {digits} digits, \
you've entered {len(user_code)}")
    else:
        return True


def check_guessed_code_against_secret_one(gen_code, digits, attempts):
    """
    Checks the code guessed by the user
    against the secret one and provides feedback.
    """
    print(f"You have a maximum of {attempts} attempts")

    while attempts > 0:
        entered_code = input(f"Enter your {digits} digits here, \
separated by a comma: \n").split(",")

        # ↓↓↓CREDIT: MicrosoftCopilot↓↓↓
        if not all(x.strip().isdigit() for x in entered_code):
            # ↑↑↑CREDIT: MicrosoftCopilot↑↑↑
            print(f"{Fore.RED}Error: \
Your code may only contain numbers!{Style.RESET_ALL}")
            continue

        guessed_code = [int(x) for x in entered_code]
        try:
            if validate_guessed_code(guessed_code, digits):
                print("The number of digits is correct!\n")
        except ValueError as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            continue

        feedback = []

        for x, y in zip(guessed_code, gen_code):
            if x in gen_code:
                if x == y:
                    feedback.append(Fore.GREEN + "O" + Style.RESET_ALL)
                else:
                    feedback.append(Fore.YELLOW + "X" + Style.RESET_ALL)
            else:
                feedback.append(Fore.RED + "-" + Style.RESET_ALL)
        if guessed_code == gen_code:
            print("Congratulations! You've cracked the code!")
            break
        else:
            attempts -= 1
            print(f"Here is your feedback: {' '.join(feedback)}\n")
            print(f"You have {attempts} attempts left\n")

    if guessed_code != gen_code and attempts == 0:
        print("Unfortunately, you're out of attempts :(.")
        print(f"The secret code is: {gen_code}")
        print("Don't worry, though! You'll get the hang of it ;)")
    return attempts


def assign_points(username, attempts_left):
    """
    Assigns 50 points to the user for each left attempt
    """
    score = attempts_left * 50
    print(f"{username}, this is your score: {score}\n")

    return score


def update_leaderboard(username, mode, score):
    """
    Updates the leaderboard with username, mode and final score
    """
    mode_worksheet = None
    row = username, score
    if mode == 1:
        mode_worksheet = SHEET.worksheet("Easy mode")
    elif mode == 2:
        mode_worksheet = SHEET.worksheet("Medium mode")
    elif mode == 3:
        mode_worksheet = SHEET.worksheet("Hard mode")
    mode_worksheet.append_row(row)
    print(f"{username}, you've been succesfully added to the leaderboard!\n")


def main():
    chosen_username = start_program()
    while True:
        start_menu_choice_def = start_rankings_quit(chosen_username)
        if start_menu_choice_def == 1:
            selected_mode = choose_mode(chosen_username)
            generated_code = generate_secret_code(selected_mode)
            feedback = check_guessed_code_against_secret_one(*generated_code)
            final_score = assign_points(chosen_username, feedback)
            update_leaderboard(chosen_username, selected_mode, final_score)
        elif start_menu_choice_def == 2:
            view_rankings()
        elif start_menu_choice_def == 3:
            start_program()


main()
