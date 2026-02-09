help =input("do you need help: ").lower()

#yes or nah

if help == "yes" or help == "y":
    print("help")

elif help == "no" or help == "n":
    print("you dont need help")

else:
    input(f"{help}yes or no?") 