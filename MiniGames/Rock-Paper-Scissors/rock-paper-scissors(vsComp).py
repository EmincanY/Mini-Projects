
def game(usName , winpoint):
    from random import randint as rd
    userPoint = 0
    compPoint = 0
    while (userPoint != winpoint) & (compPoint != winpoint) :
        userChoice = int(input(f"What's {userPoint}. your choice ? \n1. Rock\n2. Paper\n3. Scissors\n"))
        compChoice = rd(1,3)
        if userChoice == compChoice :
            print("DRAW !\n")
        elif ((userChoice == 1) & (compChoice == 3)) | ((userChoice == 2) & (compChoice == 1)) | ((userChoice == 3) & (compChoice == 2)):
            print(f"{usName} won\n")
            userPoint += 1
            print(f"{usName} score : {userPoint}\nComputer score : {compPoint}")
        else :
            print(f"Computer won\n")
            compPoint += 1
            print(f"{usName} score : {userPoint}\nComputer score : {compPoint}")

game("Emincan", 3)