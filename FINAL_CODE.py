import hlg3 #Imports the code from High Low Game
import rps3 #Imports the code from Rock Paper Scissors 

def menu(): #Menu function
    print()
    print("-------Welcome to the Game Compendium!-------")  #Introduces user to game compendium
    username = str(input("Please enter your username for this game: ")) #Asks user for their username
    print(f"\nHi {username}, Please select an option out of the following:") # Menu options
    Flag = True #Flag for the menu loop 
    while Flag is True:
        print("\n1. Rock Paper Scissors")
        print("2. High Low Game")
        print("3. Quit")

        # Code for getting user input using value errors and boundary cases
        try: 
            userInput = int(input("Enter your choice (1-3): ")) #Game selection input
            if userInput < 1 or userInput > 3: #Boundary cases
                print("Invalid input. Please enter a number from 1 to 3.") #Outputs error message
            else:
                if userInput == 1: #If the user selects option 1 it will launch Game 1
                    print("Launching Rock Paper Scissors...")
                    rps3.play_rps(username) #Calls main function from my Rock Paper Scissors file in folder
                elif userInput == 2: #If the user selects option 2 it will launch Game 2
                    print("Launching High Low Game...")
                    hlg3.play_hlg(username) #Calls main function from my High Low Game file in folder
                elif userInput == 3: #If the user selects option 3 it will quit the program
                    print(f"Thank you for playing. Goodbye {username}!") #Farewell message
                    Flag = False #Quits program
        except ValueError: #Valid integer checking
            print("Invalid input, enter a valid integer.") #Outputs error message 

menu() #Calls menu function
