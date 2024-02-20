import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    while attempts < max_attempts:
        guess = int(input("Guess the secret number (between 1 and 100): "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Incorrect guess. Try again.")
            attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
