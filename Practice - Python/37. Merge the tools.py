# Link: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Difficulty: Medium
# Solution:

def MakeUnique(argString):
    tempSet = set()
    i = 0
    newString = ""
    while( i < len(argString)):
        if(argString[i] not in tempSet):
            newString += argString[i]
            tempSet.add(argString[i])
        i += 1
    return newString


def merge_the_tools(string, k):
    myTemp = []
    tempStr = ""

    counter = 0
    for i in range(0, len(string)):
        tempStr += string[i]
        counter += 1
        if(counter == k):
            counter = 0
            myTemp.append(MakeUnique(tempStr))
            tempStr = ""
    for each in myTemp:
        print(each)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)