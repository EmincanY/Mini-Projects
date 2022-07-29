
# Computer tries numbers in the most logical way
 
def computerGuessGame(num = int(input("Please give a number between 1-100 \n"))):
    min = 0
    max = 100
    count = 1
    while True:
        computerGuess = (min+max)//2
        if computerGuess == num :
            print("Woaa, comp. found your choice {} number in {}. trying.".format(num,count))
            break
        else : 
            highOrLow = int(input("Your num is upper or lower than {} ?  ('0' lower , '1' upper)\n".format(computerGuess)))
            if highOrLow == 1 :
                min = computerGuess
                count += 1
            elif highOrLow == 0 :
                max = computerGuess
                count += 1

computerGuessGame()