import random

def getUserChoice():
    valid_choices = ['rock', 'paper', 'scissors']
    flag1 = True
    while flag1:
        try:
            user_choice = str(input("Please enter your choice 'username' (rock/paper/scissors): ").lower())
            if user_choice not in valid_choices:
                raise ValueError
            flag1 = False
            return user_choice
        except ValueError:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def getComputerChoice():
    return random.choice(['rock', 'paper', 'scissors'])

def getWinner(user_choice, computer_choice):
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

def playAgain():
    flag2 = True
    while flag2:
        try:
            play_again_input = input("\nDo you want to play again 'username'? (yes/no): ").lower()
            if play_again_input not in ['yes', 'no']:
                raise ValueError
            flag2 = False
            return play_again_input
        except ValueError:
            print("Invalid input. Please enter yes or no.")

# Main program
def play_rps():
    print("\nWelcome to Survival Rock Paper Scissors 'username'!")
    wins = 0
    continue_playing = True
    while continue_playing:
        user_choice = getUserChoice()
        computer_choice = getComputerChoice()

        winner = getWinner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        if winner == "user":
            wins += 1
            print("\nCongratulations! You win!")
        elif winner == "computer":
            print("\nSorry, you lose!")
            continue_playing = False
        else:
            print("\nIt's a draw! Let's keep playing.")

    print(f"Total wins: {wins}")
    play_again_input = playAgain()
    if play_again_input == 'yes':
        play_rps()
    else:
        print("\nThanks for playing 'username'! Returning to menu...")

play_rps()
