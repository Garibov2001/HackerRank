# Link: https://www.hackerrank.com/challenges/py-check-subset/problem
# Difficulty: Easy
# Solution:

testCases = int(input())


for i in range(0, testCases):

    input()
    setA = set(list(map(int, input().split())))

    input()
    setB = set(list(map(int, input().split())))

    if(setA.union(setB)==setB):
        print(True)
    else:
        print(False)

