# Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Difficulty: Easy
# Solution: 

input()
firstSet = set(map(int, input().split()))

input()
secondSet = set(map(int, input().split()))

newSet = firstSet.symmetric_difference(secondSet)

print(len(newSet))