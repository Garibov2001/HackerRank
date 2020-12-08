# Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Difficulty: Easy
# Solution:

numA = list(map(int, input().split()))

listA = []

for i in range(0, numA[0]):
    listA.append(input())


listB = []

for i in range(0, numA[1]):
    listB.append(input())




for i in range(0, len(listB)):
    isEnter = True
    for j in range(0, len(listA)):
        if(listA[j] == listB[i]):
            print(j+1, end=" ")
            isEnter = False
    if(isEnter):
        print(-1, end=" ")
    print()
        









