# Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Difficulty: Easy
# Solution:

studentNum = int(input())
mySum = 0
getColumn = input().split()

markIndex = 0
for i in range(0, len(getColumn)):
    if( getColumn[i] == "MARKS"):
        markIndex = i
        break


for i in range(0, studentNum):
    tempArr = input().split()
    mySum += int(tempArr[markIndex])

print(mySum/studentNum)
