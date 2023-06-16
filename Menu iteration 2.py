def menu(): #Menu function
    Flag = True #Boolean variable for loop
    while Flag == True: 
        print("-------Welcome to the Game Comependium!-------")  #Introduces user to game compendium
        print("Please select an option out of the following:")
        print("1. Rock Paper Scissors")
        print("2. High Low Game")
        print("3. Quit")

#Code for getting user input using value errors and boundary cases
        try:
            userInput = int(input("Enter your choice (1-3): "))
            if userInput < 1 or userInput > 3:
                print("Invalid input. Please enter a number between 1 and 3.")
            else:
                return userInput
        except ValueError: #
            print("Invalid input, enter a valid integer.")
gameOption = menu() #Calls menu fuction and assigns returned value to 'gameOption'

#Main program
def menu_main():
    if gameOption == 1:
        print("Launching Rock Paper Scissors...")
        #rps()
    elif gameOption== 2:
        print("Launching High Low Game...")
        #high_low_game()
    elif gameOption == 3:
        print("Thank you for playing. Goodbye!")
        quit()
menu_main()