import random
from art import logo, vs
from game_data import data

def formatted_statement(statement):
     """This takes the game data dictionary and returns the formatted statement the user will see"""
     name = statement['name']
     description = statement['description']
     country = statement['country']
     return f"{name}, a {description}, from {country}."


def compare(a_followers, b_followers, u_guess):
    """This function compares the two follower counts and returns true or false"""
    if a_followers > b_followers:
        return u_guess == "A"
    else:
        return u_guess == "B"


def game():
    """This function runs the game"""
    print(logo)
    game_over = False
    score = 0
    b_statement = random.choice(data)

    while not game_over:
        a_statement = b_statement
        b_statement = random.choice(data)
        if a_statement == b_statement:
            b_statement = random.choice(data)
        print(f"Compare A: {formatted_statement(a_statement)}")
        print(vs)
        print(f"Against B: {formatted_statement(b_statement)}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n" * 20)
        print(logo)
        if user_guess not in ("A", "B"):
            print("Invalid input. Please try again.")
            continue
        a_statement_followers = a_statement['follower_count']
        b_statement_followers = b_statement['follower_count']
        user_won = compare(a_statement_followers, b_statement_followers, user_guess)
        if user_won:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True

game()
input("\nPress enter to exit the game...")