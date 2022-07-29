# Rock - Paper - Scissors Game
def game(us1name , us2name , winpoint):
    user1point = 0
    user2point = 0
    while (user1point != winpoint) & (user2point != winpoint) :
        user1choice = int(input(f"What's {us1name}. your choice ? \n1. Rock\n2. Paper\n3. Scissors\n"))
        user2choice = int(input(f"What's {us2name}. your choice ? \n1. Rock\n2. Paper\n3. Scissors\n"))
        if user1choice == user2choice :
            print("DRAW !\n")
        elif ((user1choice == 1) & (user2choice == 3)) | ((user1choice == 2) & (user2choice == 1)) | ((user1choice == 3) & (user2choice == 2)):
            print(f"{us1name} won\n")
            user1point += 1
            print(f"{us1name} score : {user1point}\n{us2name} score : {user2point}")
        else :
            print(f"{us2name} won\n")
            user2point += 1
            print(f"{us1name} score : {user1point}\n{us2name} score : {user2point}")

game("Emincan","Alperen",3)
