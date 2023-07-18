import random #Imports random library

def getUserChoice(username):  # Function to get the user's choice for Game 1
    valid_choices = ['rock', 'paper', 'scissors'] #List that contains all the valid choices for the user to choose 
    flag1 = True # flag1 is the flag for this function used to create a loop, this initializes it as True
    while flag1: #Flag loop, while the Flag is true the loop continues - the same as all future loops
        try: #Start of try-except block
            user_choice = str(input(f"Please enter your choice {username} (rock/paper/scissors): ").lower()) #Asks the user for their choice and sets their input to lowercase
            if user_choice not in valid_choices: #Checks if the user choice is not within the valid choices list
                raise ValueError #Raises the value error and outputs the error message
            return user_choice #Returns the user choice
        except ValueError: #Value Error exception for anything another than a string 
            print("\nInvalid choice. Please enter rock, paper, or scissors.")

def getComputerChoice(): #Function to get the computer's choice for future use
    return random.choice(['rock', 'paper', 'scissors']) #Uses a list and random.choice to choose a random string within the list

def getWinner(user_choice, computer_choice): #Function that uses calculations to determine the winner
    if user_choice == computer_choice: #Checks if the user choice is equal to the computer choice 
        return "draw" #Returns "draw" to confirm  that a draw occurred
    elif ( #Block of code containing all possible winning combinations for the user
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "user" #Returns "user" to confirm that the winner is the user
    else:
        return "computer" #Returns "computer" to confirm that the computer is the winner

def playAgain(username): #Play again function that asks the user whether they would like to continue or return to the menu
    flag2 = True
    while flag2:
        try:
            play_again_input = input(f"\nDo you want to play again {username}? (yes/no): ").lower() #Asks the user if they want to play again and sets their input to lowercase
            if play_again_input not in ['yes', 'no']: #Checks if their input is within a list containing 'yes' and 'no'
                raise ValueError
            return play_again_input #Returns their play again choice 
        except ValueError: 
            print("\nInvalid input. Please enter yes or no.") #Value Error message telling the user to enter yes or no

# Main program
def play_rps(username):
    print(f"\nWelcome to Survival Rock Paper Scissors {username}!") #Welcomes the user to the game
    wins = 0 #Initializes original number of wins
    continue_playing = True #Main boolean variable that creates the overall loop for the program
    while continue_playing: #While boolean variable is True the loop will continue
        user_choice = getUserChoice(username) #Calls the function to get the users choice and assigns it to a variable
        computer_choice = getComputerChoice() #Calls the function to get the computers choice and assigns it to a variable

        winner = getWinner(user_choice, computer_choice) #Calls the function that calculates the winner based on the previous inputs

        print(f"\nYou chose: {user_choice}") #f-string output that outputs the user's choice
        print(f"The computer chose: {computer_choice}") #f-string output that outputs the computer's choice
        #Game result outputs
        if winner == "user": #Checks if the winner is the user
            wins += 1 #Adds a win to the total score
            print(f"\nCongratulations {username}! You win!") #Outputs winner message to user
        elif winner == "computer": #Checks if the winner is the computer
            print("\nSorry, you lose!") #Outputs the loss message to user
            continue_playing = False #Quits the loop by setting it to false
        else:
            print("\nIt's a draw! Let's keep playing.") #Draw output message

    print(f"Total wins: {wins}") #Displays total wins that the user has accumulated in that round

    play_again_input = playAgain(username) #Calls the play again function after the user loses to ask if they wish to play again or return to menu

    if play_again_input == 'yes': #Checks if the user does wish to play again
        play_rps(username) #Calls the main function to repeat the game 
    else:
        print(f"\nThanks for playing {username}! Returning to menu...") #This will output if they decide not to play again and the user will be returned to the menu
