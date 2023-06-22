import random

def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    flag = True
    while flag:
        try:
            user_choice = str(input("Please enter your choice 'username' (rock/paper/scissors): ").lower())
            if user_choice not in valid_choices:
                raise ValueError
            return user_choice
        except ValueError:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

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
    flag = True
    while flag:
        try:
            play_again_input = input("\nDo you want to play again 'username'? (yes/no): ").lower()
            if play_again_input not in ['yes', 'no']:
                raise ValueError
            return play_again_input
        except ValueError:
            print("Invalid input. Please enter yes or no.")

def display_result(result, user_choice, computer_choice, wins):
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    if result == "draw":
        print("It's a draw!")
    elif result == "user":
        print("Congratulations! You win!")
        wins += 1
    else:
        print("Sorry, you lose!")
    print(f"Total wins: {wins}")
    return wins

# Main program
def play_rps():
    print("\nWelcome to Survival Rock Paper Scissors 'username'!")
    wins = 0
    continue_playing = True
    while continue_playing:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            wins += 1
            print(f"\nYou chose: {user_choice}")
            print(f"The computer chose: {computer_choice}")
            print("\nCongratulations! You win!")
        elif winner == "computer":
            print(f"\nYou chose: {user_choice}")
            print(f"The computer chose: {computer_choice}")
            print("\nSorry, you lose!")
            continue_playing = False
        else:
            print(f"\nYou chose: {user_choice}")
            print(f"The computer chose: {computer_choice}")
            print("\nIt's a draw! Let's keep playing.")

    print(f"Total wins: {wins}")

    play_again_input = play_again()

    if play_again_input == 'yes':
        play_rps()
    else:
        print("\nThanks for playing 'username'! Returning to menu...")

play_rps()
