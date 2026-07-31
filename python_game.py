
import random

def number_guessing_game(best_score, player_name):
    print(f"\n---Welcome to the Number Guessing Game, {player_name}!---")

    if best_score is not None:
        print(f"Current Best Score (Min Attempts): {best_score}")

    print("\nSelect Difficult Level: ")
    print("1. Easy (1 to 10) - 5 Attempts")
    print("2. Medium (1 to 50) - 7 Attempts")
    print("3. Hard (1 to 100) - 10 Attempts")

    while True:
        try:
            choice = int(input("Enter Your Choice(1, 2, or 3): "))
            if choice == 1:
                max_num = 10
                max_attempts = 5
                break
            elif choice == 2:
                max_num = 50
                max_attempts = 7
                break
            elif choice == 3:
                max_num = 100
                max_attempts = 10
                break
            else: 
                print("Invalid Choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number: ")

    secret_number = random.randint(1, max_num)
    attempts = 0
    hint_used = False

    print(f"\nI have selected a number between 1 and {max_num}. You have {max_attempts} attempts. Good luck!")
    print("Tip: Type 'hint' if you want a clue (Can use only once!).")

    while attempts < max_attempts:
        try:
            remaining_attempts = max_attempts - attempts
            print(f"Remaining attempts: {remaining_attempts}")

            user_input = input("Enter your guess (or type 'hint'): ").lower()

            if user_input == 'hint':
                if not hint_used:
                    hint_used = True

                    if secret_number % 2 == 0:
                        print("Hint: The secret number is an EVEN numebr.")
                    else:
                        print("Hint: The secret number is an ODD number.")

                else:
                    print("You already used the hint!.")

            user_guess = int(input("Guess the number: "))
            attempts += 1

            if user_guess == secret_number:
                print("Congratulations! {player_name} You guessed the number! \nAttempts: " ,attempts)

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("New Best Score!\n")

                return best_score
            
            elif user_guess < secret_number:
                print("Too low! Guess the high number\n")
            else:
                print("Too high! Guess the low number\n")
        except ValueError:
            print("Error! Please enter thevalid number.\n")
    print(f"\nOops! {player_name}, your attempts are over! Secret numer is '{secret_number}'.")
    print("Try again next time!")
    return best_score

print("---Let's Setup You Profile---")
player_name = input("Enter your name: ").capitalize()

best_score = None

while True:        
    best_score = number_guessing_game(best_score, player_name)    

    play_again = input("Do you want try again (Yes/No): ").lower()
    if play_again != 'yes':
        print("\nGood Bye!")
        break
    print("\n" + "="*40 + "\n")            
