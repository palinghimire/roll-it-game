import random

# intialise rounds points
user_points = 0
comp_points = 0
double_user =  "no"

# Roll the dice for the user and note if they got a duble
user_one = random.randint(1, 6)
user_two = random.randint(1, 6)

if user_one == user_two:
    double_user = "yes"

# Roll the dice for the computer and note if they got a duble
comp_one = random.randint(1, 6)
comp_two = random.randint(1, 6)

#update the user and computer points
user_points += user_one + user_two
comp_points += comp_one + comp_two

#output the results
# let the user know what they rolled and if they got a double
print("\nInitial points")
print (f"user      - roll 1: {user_one} \t| roll 2: {user_two} \t| total: {user_points} ")
print (f"computer  - roll 1: {comp_one} \t| roll 2: {comp_two} \t| total: {comp_points} ")

# let the user know if they got a double
if double_user == "yes":
    print("grate news - if you win you will earn double points")
