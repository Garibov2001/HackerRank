# Link: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Difficulty: Easy
# Solution:

from itertools import permutations

getInput = input().split(" ")
length = int(getInput[1])
string = getInput[0]


permuList = list(permutations(string,length))

tempList = []
for eachTuple in permuList:
    myText = ""
    for element in eachTuple:
        myText += element
    tempList.append(myText)

tempList.sort()

for eachElement in tempList:
    print(eachElement)

    



