def integer_checker():
    """integer_checker to see if your equal to or more than 13 """


    error = "please enter a numer more or equle to 13:"

    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response
        
        except ValueError:
            print(error)

# main routine starts here
game_goal = integer_checker()
print(f"game goal is set to {game_goal}")