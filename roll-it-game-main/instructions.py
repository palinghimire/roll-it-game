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

#main routine

#ask user if they need help(check if it says yes)
help = yes_no("do you want help? ")

#display the if the user want to see instructions
if help == "yes":
    instructions()

print()
print("program continues")