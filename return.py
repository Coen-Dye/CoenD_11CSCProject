def game_function(username):
    # Use the 'username' variable in the function
    print(f"Hello, {username}! This is the game function.")

# Call the 'menu()' function and store the returned username
username = menu()

# Call the 'game_function()' and pass the 'username' as an argument
game_function(username)
