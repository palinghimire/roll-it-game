#initialise list to gold game history
game_history = []

# get data (base compontent dose this already code below fore testing purposes)
user_score = 0
comp_score = 0

while True: 
    round_played = input("round?")
    if round_played == "":
        break

    user_point = int(input("user point?"))
    comp_point = int(input("computer points?"))
    winner = input("who won? ")
    user_score = int(input("user score: "))
    comp_score = int(input("computer score: "))



    game_results = (f"round  {round_played}: user Points {user_point} | "
                    f"computer point {comp_point}, {winner} wins"
                    f"({user_score}) | {comp_score})")


    game_history.append(game_results)


print("game history")

for item in game_history:
    print(item)