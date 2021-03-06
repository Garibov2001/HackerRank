# Link: https://www.hackerrank.com/challenges/itertools-combinations/problem?h_r=next-challenge&h_v=zen
# Difficulty: Easy
# Solution:

from itertools import combinations

getInput = input().split(" ")
length = int(getInput[1])
string = getInput[0]
combList = []

for i in range(1, length + 1):
    combList.append(list(combinations(string, i)))  
    tempList = []
    for eachList in combList:
        for eachTuple in eachList:
            myText = ""
            for element in eachTuple:
                myText += element
            myText = ''.join(sorted(myText)) 
            tempList.append(myText)

    tempList.sort()
    for j in tempList:
        print(j)

    combList.pop(0)
    tempList.pop(0)
