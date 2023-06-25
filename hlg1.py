import random

def play_game():
    print("Welcome to the High Low Game!")
    print("Guess the secret number to win.")

    rounds = int(input("How many rounds do you want to play? "))

    for _ in range(rounds):
        secret_number = random.randint(1, 100)
        attempts = 9

        print("\nNew round started!")
        print("Guess a number between 1 and 100.")
    
        while attempts > 0:
            guess = int(input("Enter your guess: "))
            attempts -= 1

            if guess == secret_number:
                print("Congratulations! You guessed the secret number.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
                print(f"You have {attempts} attempts left")
            else:
                print("Too high! Try a lower number.")
                print(f"You have {attempts} attempts left")

        if attempts == 0:
            print(f"Out of attempts! The secret number was {secret_number}.")

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()
