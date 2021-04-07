Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
Difficulty: Easy

Solution:
checkSet = set(map(int, input().split()))
numTest=int(input())

result = True
for i in range(numTest):
    b = set(map(int, input().split()))
    if (len(b.difference(checkSet)) != 0): 
        result = False

print(result)