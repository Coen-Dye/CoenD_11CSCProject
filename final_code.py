import random

def menu(): #Menu function
    print()
    print("-------Welcome to the Game Compendium!-------")  #Introduces user to game compendium
    username = str(input("Please enter your username for this game: ")) 
    print(f"\nHi {username}, Please select an option out of the following:") # Menu options
    Flag = True 
    while Flag is True:
        print("\n1. Rock Paper Scissors")
        print("2. High Low Game")
        print("3. Quit")

        # Code for getting user input using value errors and boundary cases
        try:
            userInput = int(input("Enter your choice (1-3): ")) #Game selection
            if userInput < 1 or userInput > 3: #Boundary cases
                print("Invalid input. Please enter a number from 1 to 3.")
            else:
                if userInput == 1:
                    print("Launching Rock Paper Scissors...")
                    play_rps(username) #Call to rps
                elif userInput == 2:
                    print("Launching High Low Game...")
                    play_hlg() #Call to high low game
                elif userInput == 3:
                    print(f"Thank you for playing. Goodbye {username}!") #Farewell message
                    Flag = False #Quit program
        except ValueError: #Valid integer checking
            print("Invalid input, enter a valid integer.")







#Rock paper scissors code starts

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
            print("Invalid choice. Please enter rock, paper, or scissors.")

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

def play_again(username): #Play again function that asks the user whether they would like to continue or return to the menu
    flag2 = True
    while flag2:
        try:
            play_again_input = input(f"\nDo you want to play again {username}? (yes/no): ").lower()
            if play_again_input not in ['yes', 'no']:
                raise ValueError
            return play_again_input
        except ValueError:
            print("Invalid input. Please enter yes or no.")

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
            print("\nCongratulations! You win!")
        elif winner == "computer":
            print("\nSorry, you lose!")
            continue_playing = False
        else:
            print("\nIt's a draw! Let's keep playing.")

    print(f"Total wins: {wins}") #Displays total wins that the user has accumulated in that round

    play_again_input = play_again(username) #Calls the play again function after the user loses to ask if they wish to play again or return to menu

    if play_again_input == 'yes':
        play_rps(username)
    else:
        print(f"\nThanks for playing {username}! Returning to menu...") #This will output if they decide not to play again and the user will be returned to the menu








#High Low Game Code Starts

# Function to get the number of rounds to play
def getRounds():
    flag1 = True 
    while flag1:
        try:
            rounds = int(input("\nHow many rounds do you want to play?: "))
            if rounds < 1:
                raise ValueError
            flag1 = False
        except ValueError:
            print("Invalid input. Please choose at least 1 round.")
    return rounds

# Function to get the user's guess
def getGuess():
    flag2 = True
    while flag2:
        try:
            guess = int(input("Enter your guess from 1-100: "))
            if guess < 1 or guess > 100:
                raise ValueError
            flag2 = False
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 100.")
    return guess

# Function to check the user's guess against the secret number
def guessCheck(guess, secret_number, attempts):
    if guess == secret_number:
        print("\nCongratulations! You guessed the secret number.")
        return True
    elif guess < secret_number:
        print("\nToo low! Try a higher number.")
    else:
        print("\nToo high! Try a lower number.")
    print(f"You have {attempts} attempts left.")
    return False

# Function to play a single round of the game
def playRound():
    secret_number = random.randint(1, 100)
    attempts = 9

    print("\n-----Next round has begun!-----")

    flag3 = False  # Track if the guess is correct

    while attempts > 0 and flag3 == False:
        guess = getGuess()
        attempts -= 1

        flag3 = guessCheck(guess, secret_number, attempts)

    if flag3 == False:
        print(f"Out of attempts! The secret number was {secret_number}.")

# Function to ask if the player wants to play again
def playAgain():
    flag4 = True
    while flag4:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == "no":
            print("Thanks for playing!")
            return False
        elif play_again == "yes":
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main program to play the game
def play_hlg():
    print("\n----------Welcome to the High Low Game!----------")
    print("Guess the secret number from 1-100 within 9 tries to win.")
    flag5 = True
    while flag5:
        rounds = getRounds()

        for i in range(rounds):
            playRound()

        if not playAgain():
            flag5 = False
menu()
