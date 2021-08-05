import random
print("Password Generator developed by: hamid0740\nCheck github: https://github.com/hamid0740/Password-Generator\n")
while True:
    try:
        l = int(input("Enter the length of your password: "))
        break
    except:
        print("Error! Please enter only numbers.")
genpas = ""
for i in range(l):
    cht = random.randint(1, 3) # Randomly chooses character type: number (1), alphabet (2), special (3)
    if cht == 1:    # Character type: number (0-9)
        num = random.randint(0,9) # Randomly chooses number (0-9)
        genpas += str(num)
    elif cht == 2:  # Character type: alphabet (a-z , A-Z)
        alpht = random.randint(1,2) # Randomly chooses alphabet's type: lowercase (1), uppercase (2)
        alph = random.randint(1,26) # Randomly chooses alphabet (a-z)
        alphabet = ""
        if alph == 1:
            alphabet = "a"
        elif alph == 2:
            alphabet = "b"
        elif alph == 3:
            alphabet = "c"
        elif alph == 4:
            alphabet = "d"
        elif alph == 5:
            alphabet = "e"
        elif alph == 6:
            alphabet = "f"
        elif alph == 7:
            alphabet = "g"
        elif alph == 8:
            alphabet = "h"
        elif alph == 9:
            alphabet = "i"
        elif alph == 10:
            alphabet = "j"
        elif alph == 11:
            alphabet = "k"
        elif alph == 12:
            alphabet = "l"
        elif alph == 13:
            alphabet = "m"
        elif alph == 14:
            alphabet = "n"
        elif alph == 15:
            alphabet = "o"
        elif alph == 16:
            alphabet = "p"
        elif alph == 17:
            alphabet = "q"
        elif alph == 18:
            alphabet = "r"
        elif alph == 19:
            alphabet = "s"
        elif alph == 20:
            alphabet = "t"
        elif alph == 21:
            alphabet = "u"
        elif alph == 22:
            alphabet = "v"
        elif alph == 23:
            alphabet = "w"
        elif alph == 24:
            alphabet = "x"
        elif alph == 25:
            alphabet = "y"
        elif alph == 26:
            alphabet = "z"
        else:
            print("Error! Please try running the code again.")
        if alpht == 1: # Lowercase
            genpas += alphabet.lower()
        elif alpht == 2: # Uppercase
            genpas += alphabet.upper()
        else:
            print("Error! Please try running the code again.")
    elif cht == 3:  # Character type = special (!, @, #, $, &)
        spcl = random.randint(1,5) # Randomly chooses special: ! (1), @ (2), # (3), $ (4), & (5)
        if spcl == 1:
            genpas += "!"
        elif spcl == 2:
            genpas += "@"
        elif spcl == 3:
            genpas += "#"
        elif spcl == 4:
            genpas += "$"
        elif spcl == 5:
            genpas += "&"
        else:
            print("Error! Please try running the code again.")
    else:
        print("Error! Please try running the code again.")
print("The generated password is: " + genpas) # Prints the final generated password
