import random

def show_instructions():
    print("Welcome to the High Low Game!")
    print("Guess the secret number to win.")

def get_rounds():
    rounds_flag = True
    while rounds_flag:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds < 1:
                raise ValueError
            rounds_flag = False
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return rounds

def generate_secret_number():
    return random.randint(1, 100)

def get_guess(attempts):
    guess_flag = True
    while guess_flag:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                raise ValueError
            guess_flag = False
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
    return guess

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

    guess_correct = False  # Track if the guess is correct

    while attempts > 0 and guess_correct == False:
        guess = get_guess(attempts)
        attempts -= 1

        guess_correct = check_guess(guess, secret_number, attempts)

    if guess_correct == False:
        print(f"Out of attempts! The secret number was {secret_number}.")

def play_again():
    play_again_flag = True
    while play_again_flag:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "no":
            print("Thanks for playing!")
            return False
        elif play_again.lower() == "yes":
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
#main program
def play_game():
    show_instructions()
    mainFlag = True
    while mainFlag:
        rounds = get_rounds()

        for _ in range(rounds):
            play_round()

        if not play_again():
            mainFlag = False

# Start the game
play_game()
