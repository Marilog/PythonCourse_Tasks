def is_uppercase(inp):
    if inp == " ":
        return True
    elif inp.isdigit() and inp.isupper():
        return True
        
    return inp.isupper()