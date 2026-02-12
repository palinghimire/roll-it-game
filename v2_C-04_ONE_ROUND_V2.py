import random

def initialise_points(which_player):
    """roll the dice for the user and note if they got a duble"""
    # Roll the dice for the user and note if they got a duble
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    double = "yes" if roll_one == roll_two else "no"

    total_points = roll_one + roll_two
    print(f"{which_player} - roll 1: {roll_one} and roll 2: {roll_two} for a total of {total_points}")

    return total_points, double


def make_statment(statement, decoration):
    """add emojis to the statment"""

    end = decoration * 3 
    print(f"\n{end} {statement} {end}")
#main starts here

# roll the dice for the user and note if they got a double
initialise_user = initialise_points("user")
initialise_comp = initialise_points("comp")


user_points = initialise_user[0]
comp_points = initialise_comp[0]

user_double = initialise_user[1]
comp_double = initialise_comp[1]

# let the user know if they got a double
if user_double == "yes":
    print("great news - if you win you will earn double points")

#asume user will go first...
first = "user"
second = "comp"
player_1_points = user_points
player_2_points = comp_points

#if the user has fewer points they start first
if user_points < comp_points:
    print("you start because your initial roll was lower then the computer\n")

#if the computer roll equal point the user is player 1
elif user_points == comp_points:
    print("the initial rolls were the same, the user starts!")

#if the computer has fewer points they start first and player 1 becomes the computer
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first 

#loop until one of the players wins 
while player_1_points < 13 and player_2_points < 13:
    print()
    input("print ENTER to continue the round")

    #FIst player rolls the dice and points are updated
    PLAYER_1_ROLL = random.randint(1, 6)
    player_1_points += PLAYER_1_ROLL
    print(f"{first}: rolled a {PLAYER_1_ROLL} has {player_1_points} points")

    #if a persons score is over 13 end the round
    if player_1_points >= 13:
        break
    #second player rolls the dice and points are updated
    PLAYER_2_ROLL = random.randint(1, 6)
    player_2_points += PLAYER_2_ROLL

#output the results
    print(f"{second}: rolled a {PLAYER_2_ROLL} has {player_2_points} points")

    print(f"{first}: {player_1_points} | {second} {player_2_points} points")

#print("end of round")    
user_points = player_1_points
comp_points = player_2_points

if first == "comp":
    user_points, comp_points = comp_points, user_points

#WORK OUT WHO WON
if user_points > comp_points:
    WINNER = "user"
else:
        WINNER = "comp"

round_feedback =f"the{WINNER} won"

#double points if the user got a double
if WINNER == "user" and user_double == "yes":
    user_points = user_points * 2


#output the results
make_statment(statement = "end of round", decoration="=")
print(f"Round feedback: {round_feedback}")
print(f"Final scores - User: {user_points}, Computer: {comp_points}")