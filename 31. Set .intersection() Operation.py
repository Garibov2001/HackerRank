# Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Difficulty: Easy
# Solution:

input()
firstSet = set(map(int, input().split()))

input()
secondSet = set(map(int, input().split()))

newSet = firstSet.intersection(secondSet)

print(len(newSet))