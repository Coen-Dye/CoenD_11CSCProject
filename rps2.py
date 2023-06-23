import random
option= ('r','p','s')

def RPS():
    user_score = 0
    while True:
        user_choice = input('Enter your choice R or P or S : ')
        computer_choice = random.choice(option)

        print('user chose ' ,user_choice)
        print('computer chose ',computer_choice)


        if user_choice == 'r':
            if computer_choice == 's':
                print("You Win")
                user_score = user_score + 1
            elif computer_choice == 'p':
                print()
                print("You Lose")
                print()
                print("Your score was",user_score)
                print("======================================================================")
            else:
                print("you Drew")
                
        if user_choice == 'p':
            if computer_choice == 'r':
                print("You Win")
                user_score = user_score + 1
            elif computer_choice == 's':
                print()
                print("You Lose")
                print()
                print("Your score was",user_score)
                print("======================================================================")
            else:
                print("you Drew")
                
        if user_choice == 's':
            if computer_choice == 'p':
                print("You Win")
                user_score = user_score + 1
            elif computer_choice == 'r':
                print()
                print("You Lose")
                print()
                print("Your score was",user_score)
                print("======================================================================")

            else:
                print("you Drew")

RPS()

    

