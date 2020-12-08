# Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?h_r=next-challenge&h_v=zen
# Difficulty: Easy
# Solution:

input()
firstSet = set(map(int, input().split()))

input()
secondSet = set(map(int, input().split()))

newSet = firstSet.difference(secondSet)

print(len(newSet))