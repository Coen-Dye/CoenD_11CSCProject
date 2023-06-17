def menu():
    Flag = True
    while Flag:
        print()
        print("-------Welcome to the Game Comependium!-------")  #Introduces user to game compendium
        print("Please select an option out of the following:")
        print("1. Rock Paper Scissors")
        print("2. High Low Game")
        print("3. Quit")
        
        try:
            userInput = int(input("Enter your choice (1-3): ")) 
            if userInput < 1 or userInput > 3:
                print("Invalid input. Please enter a number between 1 and 3.")
            else:
                return userInput
        except ValueError:
            print("Invalid input, enter a valid integer.")

gameOption = menu()