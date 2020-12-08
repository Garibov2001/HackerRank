# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?h_r=next-challenge&h_v=zen
# Difficulty: Easy
# Solution: 


def GetInput():
    myList = input().split()
    return myList


input()

mySet = set(tuple(map(int, input().split())))

numCommands = int(input())

for i in range(0, numCommands):
    userInp = GetInput()
    if(userInp[0] == "pop"):
        mySet.pop()
    else:
        if(userInp[0] == "remove"):
            mySet.remove(int(userInp[1]))
        else:
            if(userInp[0] == "discard"):
                mySet.discard(int(userInp[1]))

print(sum(mySet))