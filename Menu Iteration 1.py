def menu():
    Flag = True
    while Flag:
        print()
        print("-------Welcome to the Game Comependium!-------")  #Introduces user to game compendium
        print("Please select an option out of the following:")
        print("1. Rock Paper Scissors")
        print("2. High Low Game")
        print("3. Quit")

        userInput = int(input("Select your variable from 1 to 3 (1 - Rock Paper Scissors, 2 - High Low Game, 3 - Quit): "))
        if userInput == 3:
            print("Goodbye!")
            Flag = False
        elif userInput in [1, 2]:
            return userInput
        else:
            print("Invalid integer. Please enter a number from 1 to 3")
            
menu()