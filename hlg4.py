import random

def show_instructions():
    print("Welcome to the High Low Game!")
    print("Guess the secret number to win.")

def get_rounds():
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return rounds

def generate_secret_number():
    return random.randint(1, 100)

def get_guess(attempts):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                raise ValueError
            return guess
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

def check_guess(guess, secret_number, attempts):
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        return True
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
    print(f"You have {attempts} attempts left")
    return False

def play_round():
    secret_number = generate_secret_number()
    attempts = 9

    print("\nNew round started!")
    print("Guess a number between 1 and 100.")

    while attempts > 0:
        guess = get_guess(attempts)
        attempts -= 1

        if check_guess(guess, secret_number, attempts):
            return

    print(f"Out of attempts! The secret number was {secret_number}.")

def play_game():
    show_instructions()
    rounds = get_rounds()

    for _ in range(rounds):
        play_round()

    while True:
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() == "no":
            print("Thanks for playing!")
            return
        elif play_again.lower() != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")

# Start the game
play_game()