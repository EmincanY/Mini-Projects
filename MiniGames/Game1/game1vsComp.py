# Game1 Player vs Computer mode. 
# Player will tell a number
# Computer will tell a number too.(Same length with player's number)
# Player and Computer number's have looked at the divisors.
# They will earn as many points as the divisor of the number they said.
# Player will determine how many rounds there will be and also player can quit whenever someone want.

from random import randint


def numOfDivisors(num):
    counter = 0
    for i in range(1, num+1):
        if num % i == 0:
            counter += 1
    return counter


def game1VsComp(p1 = input("What's the player name ?\n")):
    p1choice = 0
    p1point = 0
    compoint = 0
    round = 1
    round_lim = int(input("How many rounds does the game last ?\n"))
    import random as rd
    digit_length = rd.randint(2,5)
    while (round <= round_lim):
        p1choice = input(f"What's your {digit_length} digits number {p1} ? (if you wan't to finish the game press 'q')")
        compChoice = randint(len(str(digit_length)) , len(str(digit_length))+1)
        if p1choice == "q":
            print(f"{p1} = {p1point} \nComputer = {compoint}\nTotal round :{round-1}")
            break
        elif len(p1choice) == digit_length :
            p1point += numOfDivisors(int(p1choice))
            compoint += numOfDivisors(compChoice)
            print(f"{p1} = {p1point} \nComputer = {compoint}\n{round}. round done.")
            round += 1
    print("Game Finish !")
    if p1point > compoint:
        print(f"Congrats {p1}")
    elif compoint > p1point:
        print(f"Unfortunately, Computer won :( ")
    else:
        print("Draw")
        
game1VsComp()
