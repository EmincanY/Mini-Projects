def factorial(num):
    if (num < 0) | (type(num) != int) :
        raise ValueError("You didin't enter a number which could have factorial")
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
