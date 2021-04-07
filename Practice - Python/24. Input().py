# Link: https://www.hackerrank.com/challenges/input/problem
# Difficulty: Easy
# Solution:

firstList = list(map(int, input().split()))
x = firstList[0]
polynomialResult = eval(input())

if(polynomialResult == firstList[1]):
    print(True)
else:
    print(False)

