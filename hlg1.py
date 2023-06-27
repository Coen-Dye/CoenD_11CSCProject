import random

def play_game():
    print("Welcome to the High Low Game!")
    print("Guess the secret number to win.")

    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for _ in range(rounds):
        secret_number = random.randint(1, 100)
        attempts = 9

        print("\nNew round started!")
        print("Guess a number between 1 and 100.")

        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
                if guess < 1 or guess > 100:
                    raise ValueError
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
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 100.")

        if attempts == 0:
            print(f"Out of attempts! The secret number was {secret_number}.")

    while True:
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() == "yes":
            break
        elif play_again.lower() == "no":
            print("Thanks for playing!")
            return
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    play_game()

# Start the game
play_game()
