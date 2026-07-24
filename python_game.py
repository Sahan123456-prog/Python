import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number between 1 and 10: "))
        attempts += 1

        if user_guess == secret_number:
            print("Congratulations! You guessed the number! Attempts: " ,attempts)
            break
        elif user_guess < secret_number:
            print("Too low! Guess the high number")
        else:
            print("Too high! Guess the low number")

number_guessing_game()                