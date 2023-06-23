import random

valid_choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in valid_choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(valid_choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "user"
    else:
        return "computer"

def play_again():
    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    while play_again_input not in ['yes', 'no']:
        print("Invalid input. Please enter yes or no.")
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
    return play_again_input == 'yes'

#main program
def rps():
    print("Welcome to Rock Paper Scissors!")
    Flag = True
    while Flag:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(user_choice, computer_choice)
        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose!")

        if not play_again():
            Flag = False

    print("Thanks for playing!")

rps()