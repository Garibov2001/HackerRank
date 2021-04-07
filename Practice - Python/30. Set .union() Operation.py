# Link: https://www.hackerrank.com/challenges/py-set-union/problem
# Difficulty: Easy
# Solution:

input()
firstSet = set(map(int, input().split()))
input()
secondSet = set(map(int, input().split()))

newSet = firstSet.union(secondSet)

print(len(newSet))
