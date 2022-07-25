# This game is a 2 players game.
# Players will tell the numbers with same digits.
# We will look at the divisors of the 2 numbers they said.
# They will earn as many points as the divisor of the number they said.
# They will determine how many rounds there will be but they can quit whenever someone want.


def numOfDivisors(num):
    counter = 0
    for i in range(1, num+1):
        if num % i == 0:
            counter += 1
    return counter


def game1(p1=input("What's Player 1 name ?\n"), p2=input("What's Player 2 name ?\n")):
    p1choice = 0
    p2choice = 0
    p1point = 0
    p2point = 0
    round = 1
    round_lim = int(input("How many rounds does the game last ?\n"))
    import random as rd
    digit_length = rd.randint(2,5)
    while (round <= round_lim):
            p1choice = input(
                f"What's your {digit_length} digits number {p1} ? (if you wan't to finish the game press 'q')")
            p2choice = input(
                f"What's your {digit_length} digits number {p2} ? (if you wan't to finish the game press 'q')")
            if (p1choice == "q") | (p2choice == "q") :
                print(f"{p1} = {p1point} \n{p2} = {p2point}\nTotal round :{round-1}.\nGame Finish.")
                break
            elif (len(p1choice)==len(p2choice)==digit_length):
                p1point += numOfDivisors(int(p1choice))
                p2point += numOfDivisors(int(p2choice))
                print(f"{p1} = {p1point} \n{p2} = {p2point}\n{round}. round done.")
                round += 1
                
    if p1point > p2point:
        print(f"Congrats {p1}")
    elif p2point > p1point:
        print(f"Congrats {p2}")
    else:
        print("Draw")


game1()









