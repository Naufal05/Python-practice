#Display art
from art import logo
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account['name']
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
print(logo)
score = 0
game_should_continue = True
# generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}.")
    print("vs")
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(guess, account_a['follower_count'], account_b['follower_count'])

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:      
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False