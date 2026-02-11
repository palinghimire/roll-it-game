
while True:
    name = input("whats your name:")

    if name == "" or name == " ":
        print ("please enter a name")
        continue

    help =input(f"{name} do you need help: ").lower()

    #yes or nah
    if help == "yes" or help == "y":
        print("help")
        break
    elif help == "no" or help == "n":
        print("you dont need help")
        break
    else:
        print("yes or no?") 
        continue

print("we are done")