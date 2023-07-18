import random #Imports random library

# Function to get the number of rounds to play
def getRounds(username):
    flag1 = True #Sets flag to true to initiate the loop
    while flag1: #This is a flag loop that will keep running while the Flag is set to True
        try:
            rounds = int(input(f"\nHow many rounds do you want to play {username}?: ")) #Asks user the amount of rounds they want to play
            if rounds < 1: #Checks if the input is a negative number
                raise ValueError #Raises the Value Error at the end of this block of code because the input was invalid
            flag1 = False #sets flag to false to exit the loop
        except ValueError: #Value Error exception
            print("\nInvalid input. Please choose at least 1 round.") #Outputs Error message
    return rounds #Returns user's selected number of rounds

# Function to get the user's guess
def getGuess(username):
    flag2 = True
    while flag2:#Flag loop while flag = True
        try:
            guess = int(input(f"{username}, Enter your guess from 1-100: ")) #User input for their guess between 1-100
            if guess < 1 or guess > 100: #Process for boundary checking of numbers outside 1-100
                raise ValueError 
            flag2 = False #Sets flag to false to exit loop
        except ValueError:
            print("\nInvalid input. Please enter a number from 1-100") #Output error message
    return guess #Returns user's guess

# Function to check the user's guess against the secret number
def guessCheck(guess, secret_number, attempts, username):
    if guess == secret_number: #Checks guess against secret number
        print(f"\nCongratulations {username}! You guessed the secret number.") #Congratulations message and uses f-strings to address the user by their username, as done throughout the rest of the code
        return True #Returns flag3 to True in the 'playRound' function
    elif guess < secret_number: #Checks if the guess is lower than the secret number
        print("\nToo low! Try a higher number.") #Tells the user their guess is too low
    else: #If it isn't too low or the correct number, then it will be too high
        print("\nToo high! Try a lower number.") #Tells the user their guess is too high
    print(f"You have {attempts} attempts left.") #Displays attempts left
    return False #Returns the value of flag3 in 'playRound' function to False

# Function to play a single round of the game
def playRound(username):
    secret_number = random.randint(1, 100) #Generates a secret number between 1-100 and assigns it to a variable called 'secret_number'
    attempts = 9 #Initializes attempts value to 9

    print("\n-----Next round has begun!-----")

    flag3 = False  # Track if the guess is correct

    while attempts > 0 and flag3 == False: #A loop that only continues when the attempts are above 0 AND flag3 is False from the 'guessCheck' function which is called a few lines below
        guess = getGuess(username) #Calls 'getGuess' function to get the user's guess
        attempts -= 1 #Lowers attempts by one

        flag3 = guessCheck(guess, secret_number, attempts, username) #Calls guessCheck to check the user's guess and assigns it to flag3 to be either True or False to continue or break the loop

    if flag3 == False: #Checks if flag3 is false
        print(f"Out of attempts! The secret number was {secret_number}.") #Out of attempts message and uses f-string to display secret number

# Function to ask if the player wants to play again
def playAgain(username):
    flag4 = True
    while flag4:
        play_again = input(f"\nDo you want to play again {username}? (yes/no): ").lower() #Asks the user if they want to play again and sets it to lowercase
        if play_again == "no": #Checks if the user chose 'no'
            print("Thanks for playing!") 
            return False #Returns False to exit loop
        elif play_again == "yes": #Checks if the user chose 'yes'
            return True #Returns True to exit loop
        else:
            print("Invalid input. Please enter 'yes' or 'no'.") #Invalid input message because the program won't accept anything other than yes or no

# Main program to play the game
def play_hlg(username):
    print(f"\n----------Welcome to the High Low Game {username}!----------") #Welcomes user to the game 
    print("Guess the secret number from 1-100 within 9 tries to win.") #Displays game instructions
    flag5 = True
    while flag5:
        rounds = getRounds(username) #Gets the number of rounds by calling the 'getRounds' function

        for i in range(rounds): #Loop to carry out the number of rounds
            playRound(username) #Calls the function for a single round

        play = playAgain(username) #Calls play again function
        if play == False: 
            flag5 = False


