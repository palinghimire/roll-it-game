error = "please enter a numer more or equle to 13:"

while True:
    try:
        game_goal = int(input("what is the game goal? "))

        if game_goal < 13:
            print(error)
        else:
            print(f"game_goal has been set to {game_goal}")
            break

    except ValueError:
        print(error)