def factorial(a): 
    if type(a) == int : 
        if a < 0: 
            return "Undefined" 
        elif (a == 0) or (a == 1): 
            return 1 
        else: 
            return a*factorial(a-1)
    else : 
        print('Please enter a integer number ! .')