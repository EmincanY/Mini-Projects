# Fibonacci list = [1,1,2,3,5,8,13,21,....] 

def fiboListCreator(lenght):
    fiboList = [1,1]
    for i in range(lenght-2):
        newNum = fiboList[i] + fiboList[i+1]
        fiboList.append(newNum)
    return fiboList

print(fiboListCreator(8))
