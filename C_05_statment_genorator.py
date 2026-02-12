def make_statment(statement, decoration):
    """add emojis to the statment"""

    end = decoration * 3 
    print(f"{end} {statement} {end}")


#main routine
make_statment(statement = "hello world", decoration="*")
make_statment(statement = "python is great", decoration="^")