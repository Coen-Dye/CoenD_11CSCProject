def menu(): #Menu function
    Flag = True 
    while Flag is True:  #Flag loop
        print()
        print("-------Welcome to the Game Compendium!-------")  #Introduces user to game compendium
        username = str(input("Please enter your username: ")) 
        print()
        print(f"Hi {username}, Please select an option out of the following:") # Menu options
        print("1. Rock Paper Scissors")
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
                    rps() #Call to rps
                elif userInput == 2:
                    print("Launching High Low Game...")
                    high_low_game() #Call to high low game
                elif userInput == 3:
                    print(f"Thank you for playing. Goodbye {username}!") #Farewell message
                    Flag = False #Quit program
        except ValueError: #Valid integer checking
            print("Invalid input, enter a valid integer.")
    return username #Returns username for future functions

username = menu()