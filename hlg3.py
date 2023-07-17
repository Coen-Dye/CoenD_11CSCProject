import random

# Function to get the number of rounds to play
def getRounds(username):
    flag1 = True 
    while flag1:
        try:
            rounds = int(input(f"\nHow many rounds do you want to play {username}?: "))
            if rounds < 1:
                raise ValueError
            flag1 = False
        except ValueError:
            print("\nInvalid input. Please choose at least 1 round.")
    return rounds

# Function to get the user's guess
def getGuess(username):
    flag2 = True
    while flag2:
        try:
            guess = int(input(f"{username}, Enter your guess from 1-100: "))
            if guess < 1 or guess > 100:
                raise ValueError
            flag2 = False
        except ValueError:
            print("\nInvalid input. Please enter a number from 1-100")
    return guess

# Function to check the user's guess against the secret number
def guessCheck(guess, secret_number, attempts, username):
    if guess == secret_number:
        print(f"\nCongratulations {username}! You guessed the secret number.")
        return True
    elif guess < secret_number:
        print("\nToo low! Try a higher number.")
    else:
        print("\nToo high! Try a lower number.")
    print(f"You have {attempts} attempts left.")
    return False

# Function to play a single round of the game
def playRound(username):
    secret_number = random.randint(1, 100)
    attempts = 9

    print("\n-----Next round has begun!-----")

    flag3 = False  # Track if the guess is correct

    while attempts > 0 and flag3 == False:
        guess = getGuess(username)
        attempts -= 1

        flag3 = guessCheck(guess, secret_number, attempts, username)

    if flag3 == False:
        print(f"Out of attempts! The secret number was {secret_number}.")

# Function to ask if the player wants to play again
def playAgain(username):
    flag4 = True
    while flag4:
        play_again = input(f"\nDo you want to play again {username}? (yes/no): ").lower()
        if play_again == "no":
            print("Thanks for playing!")
            return False
        elif play_again == "yes":
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main program to play the game
def play_hlg(username):
    print(f"\n----------Welcome to the High Low Game {username}!----------")
    print("Guess the secret number from 1-100 within 9 tries to win.")
    flag5 = True
    while flag5:
        rounds = getRounds(username)

        for i in range(rounds):
            playRound(username)

        play = playAgain(username)
        if play == False:
            flag5 = False


