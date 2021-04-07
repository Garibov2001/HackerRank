# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Difficulty: Easy
# Solution: 

def MaxNumber (argList):
    maxNumber = argList[0]
    for i in range(1,len(argList)):
        if(argList[i] > maxNumber):
            maxNumber = argList[i]
    return maxNumber

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


    myList = []
    myList = [x for x in arr]

    maxNumber = MaxNumber(myList)

    i = 0
    while(i < len(myList)):
        if(myList[i] == maxNumber):
            myList.pop(i)
        else:
            i += 1
    maxNumber = MaxNumber(myList)

    print(maxNumber)
    
