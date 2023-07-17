#This is not the final code, this is just the original code of the menu without the imports of other files for Game 1 and 2, to show my progress and how the project all began.

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
menu()
