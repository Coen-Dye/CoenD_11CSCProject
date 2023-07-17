import random

def getUserChoice(username):  # Function to get the user's choice for Game 1
    valid_choices = ['rock', 'paper', 'scissors']
    flag1 = True # flag1 is the flag for this function used to create a loop
    while flag1:
        try:
            user_choice = str(input(f"Please enter your choice {username} (rock/paper/scissors): ").lower())
            if user_choice not in valid_choices:
                raise ValueError #Raises the value error and outputs the error message
            return user_choice
        except ValueError:
            print("\nInvalid choice. Please enter rock, paper, or scissors.")

def getComputerChoice(): #Function to get the computer's choice for future use
    return random.choice(['rock', 'paper', 'scissors']) #Uses a list and random.choice to choose a random string within the list

def getWinner(user_choice, computer_choice): #Function that uses calculations to determine the winner
    if user_choice == computer_choice:
        return "draw"
    elif ( #Block of code containing all possible winning combinations for the user
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "user"
    else:
        return "computer"

def playAgain(username): #Play again function that asks the user whether they would like to continue or return to the menu
    flag2 = True
    while flag2:
        try:
            play_again_input = input(f"\nDo you want to play again {username}? (yes/no): ").lower()
            if play_again_input not in ['yes', 'no']:
                raise ValueError
            return play_again_input
        except ValueError:
            print("\nInvalid input. Please enter yes or no.")

# Main program
def play_rps(username):
    print(f"\nWelcome to Survival Rock Paper Scissors {username}!")
    wins = 0
    continue_playing = True #Main boolean variable that creates the overall loop for the program
    while continue_playing:
        user_choice = getUserChoice(username) #Calls the function to get the users choice
        computer_choice = getComputerChoice() #Calls the function to get the computers choice

        winner = getWinner(user_choice, computer_choice) #Calls the function that calculates the winner based on the previous inputs

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        #Game result outputs
        if winner == "user":
            wins += 1
            print(f"\nCongratulations {username}! You win!")
        elif winner == "computer":
            print("\nSorry, you lose!")
            continue_playing = False
        else:
            print("\nIt's a draw! Let's keep playing.")

    print(f"Total wins: {wins}") #Displays total wins that the user has accumulated in that round

    play_again_input = playAgain(username) #Calls the play again function after the user loses to ask if they wish to play again or return to menu

    if play_again_input == 'yes':
        play_rps(username)
    else:
        print(f"\nThanks for playing {username}! Returning to menu...") #This will output if they decide not to play again and the user will be returned to the menu
