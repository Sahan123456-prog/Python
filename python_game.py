
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    print("\nSelect Difficult Level: ")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    while True:
        try:
            choice = int(input("Enter Your Choice(1, 2, or 3): "))
            if choice == 1:
                max_num = 10
                break
            elif choice == 2:
                max_num = 50
                break
            elif choice == 3:
                max_num = 100
                break
            else: 
                print("Invalid Choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number: ")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 10: "))
            attempts += 1

            if user_guess == secret_number:
                print("Congratulations! You guessed the number! Attempts: " ,attempts)
                break
            elif user_guess < secret_number:
                print("Too low! Guess the high number\n")
            else:
                print("Too high! Guess the low number\n")
        except ValueError:
            print("Error! Please enter thevalid number.\n")

while True:        
    number_guessing_game()    

    play_again = input("Do you want try again (Yes/No): ").lower()
    if play_again != 'yes':
        print("\nGood Bye!")
        break
    print("\n" + "="*40 + "\n")            
