# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=next-challenge&h_v=zen
# Difficulty: Easy

# Solution:

theNumberofM = int(input())
M = set(map(int, input().split()))

theNumberofN = int(input())
N = set(map(int, input().split()))

differenceSet = set()

differenceSet.update(M.difference(N))
differenceSet.update(N.difference(M))

differenceSet = list(differenceSet)
differenceSet.sort()

for element in differenceSet:
    print(element)





