#This is not the final code, this is just the original code of the menu without the imports of other files for Game 1 and 2, to show my progress and how the project all began.

def menu(): #Menu function
    print()
    print("-------Welcome to the Game Compendium!-------")  #Introduces user to game compendium
    username = str(input("Please enter your username for this game: ")) 
    print(f"\nHi {username}, Please select an option out of the following:") # Menu options
    Flag = True #Intitializes menu loop Flag
    while Flag is True: #While the flag is true the menu loop will continue
        #Three menu options
        print("\n1. Rock Paper Scissors")
        print("2. High Low Game")
        print("3. Quit")

        # Code for getting user input using value errors and boundary cases
        try:
            userInput = int(input("Enter your choice (1-3): ")) #Game selection, asks user to enter their menu choice
            if userInput < 1 or userInput > 3: #Boundary cases checking
                print("Invalid input. Please enter a number from 1 to 3.") #If it is outside the boundary, output error message 
            else:
                if userInput == 1: #Checks if the user input is 1
                    print("Launching Rock Paper Scissors...") #Tells the user RPS is launching
                    play_rps(username) #Call to rps
                elif userInput == 2: #Checks if the user input is 2
                    print("Launching High Low Game...") #Tells the user HLG is launching
                    play_hlg() #Call to high low game
                elif userInput == 3: #Checks if the user input is 3
                    print(f"Thank you for playing. Goodbye {username}!") #Farewell message
                    Flag = False #Quits program
        except ValueError: #Valid integer checking
            print("Invalid input, enter a valid integer.")
menu() #Original call to menu
