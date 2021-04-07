# Link: https://www.hackerrank.com/challenges/python-lists/problem
# Difficulty: Easy
# Solution:

def ReadLine(argText):
    newText = argText.split(" ")
    return newText


def RemoveElement(element):
    i = 0
    while (i < len(myArr)):
        if(myArr[i] == element):
            myArr.pop(i)
            return 
        else:
            i += 1


if __name__ == '__main__':
    myArr = []
    N = int(input())
    while (N > 0):
        getInput = input()
        inpArr = ReadLine(getInput)
        if(inpArr[0] == "insert"):
            myArr.insert(int(inpArr[1]), int(inpArr[2]))
        elif(inpArr[0] == "print"):
            print(myArr)
        elif(inpArr[0] == "remove"):
            RemoveElement(int(inpArr[1]))
        elif(inpArr[0] == "append"):
            myArr.append(int(inpArr[1]))
        elif(inpArr[0] == "sort"):
            myArr.sort()
        elif(inpArr[0] == "pop"):
            myArr.pop(len(myArr) - 1)
        elif(inpArr[0] == "reverse"):
            myArr.reverse()
        N -= 1
        


        