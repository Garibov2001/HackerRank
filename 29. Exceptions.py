# Link: https://www.hackerrank.com/challenges/exceptions/problem
# Difficulty: Easy
# Solution:

numTest = int(input())


for i in range(0, numTest):
    
    try:
        getInput = list(map(int, input().split()))
        print(round(getInput[0]/getInput[1]))

    except ZeroDivisionError as e:
        print ("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print ("Error Code:",e)
