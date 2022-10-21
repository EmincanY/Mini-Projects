def factorial(num) :
  if type(num) == int :
    if num >= 2 :
      result = 1
      for i in range(1,num+1):
        result *= i
      return result
    elif num == 0 or num == 1 :
      return 1
    else : 
      return 'The Factorial of negative numbers are undefined.'
  else : 
    return 'Please enter a integer value !'

