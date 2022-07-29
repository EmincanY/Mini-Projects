#Guessing Game. need to find the number between 1-100


def numGame2(chance = 5):
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
        elif (count == chance) & (userGuess != num) :
            print(f"You couldn't guess correctly even though you tried {count} times")
            break
        
numGame2(8)