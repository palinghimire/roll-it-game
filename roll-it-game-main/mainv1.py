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


#main routine

#testing loop
while True:
    help = yes_no("do you want to see the instructions")
    print(f"you picked {help}")

print("we are done")