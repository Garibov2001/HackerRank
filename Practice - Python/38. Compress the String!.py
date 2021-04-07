# Link: https://www.hackerrank.com/challenges/compress-the-string/problem
# Difficulty: Medium
# Solution:

myString = input()
counter = 1
for i in range(0, len(myString)):
    if( i!= len(myString) - 1 and myString[i] == myString[i + 1]):
        counter += 1 
    else:
        print(f'({counter}, {myString[i]})', end=" ")
        counter = 1
