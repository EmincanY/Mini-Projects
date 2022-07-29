# Guessing Game. You have 5 chance to find correct number between 1-100


def numGame1():
    from random import randint as rd
    num = rd(1,100)
    print(num)
    count = 0
    while True:
        userGuess = int(input(f"Please tell {count+1}. your guess : "))
        count += 1
        if userGuess == num :
            print(f"Congrats you found the number we are looking for in {count}th guess.")
            break
        elif (count == 5) & (userGuess != num) :
            print("You couldn't guess correctly even though you tried 5 times")
            break
        
numGame1()




