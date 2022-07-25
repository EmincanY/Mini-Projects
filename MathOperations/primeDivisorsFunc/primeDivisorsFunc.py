# Prime Divisors find.
def isPrime(num):
    from math import sqrt as sqrt
    if num < 2 or type(num) == float:
        return False
    else:
        for i in range(2, int(sqrt(num)+1)):
            if num % i == 0:
                return False
        return True

def primeDivisors(num):
    primeDivisors = []
    for i in range(2,num):
        if (num % i == 0) & (isPrime(i)):
            primeDivisors.append(i)
    return primeDivisors
