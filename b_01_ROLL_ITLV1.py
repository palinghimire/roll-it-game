#funchtions 

def yes_no(question):

    """checks if it outputs yes or no"""

    while True:


        response = input("do you need help: ").lower()

        #yes or nah
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return("no")
        else:
            print("yes or no?") 


def instructions():
    """prints instructions"""

    print("""
*** instructions ***
      
Roll the dice and try to win!
    """)


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
#main routine

#ask user if they need help(check if it says yes)
help = yes_no("do you want help? ")

#display the if the user want to see instructions
if help == "yes":
    instructions()

print()
game_goal = integer_checker()
print(f"game goal is set to {game_goal}")