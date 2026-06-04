import random
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
    #Function to the Check the guess_number aganist actual answer
    def check_answer(user_guess, actual_answer):
        if user_guess > actual_answer:
            print("Too high.")
        elif user_guess < actual_answer:
            print("Too low.")
        else:
            print(f"You got it right! The answer was {actual_answer}.")

    # fucntion to set difficulty
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS

    # Choosing a number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)



    # Let the user guess a number
    guess = int(input("Make a guess: "))
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number")

    # track the number of turns and reduce by 1 if they get it wrong

    # Repeat the guessing functionality if they get it wrong
    while guess != answer:
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)


game()