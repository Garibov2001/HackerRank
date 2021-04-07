# Link: https://www.hackerrank.com/challenges/any-or-all/problem
# # Difficulty: Easy

# Solution:
def isPositive(myList):
    isPositiveList = []
    for i in range(0, len(myList)):
        if(int(myList[i])>0):
            isPositiveList.append(True)
        else:
            isPositiveList.append(False)
            return isPositiveList
    return isPositiveList

def isPolindrome(myList):
    for i in range(0, len(myList)):
        if(myList[i] ==  myList[i][::-1]):
            return True
    return False

    
input()
tempList = input().split()

if(all(isPositive(tempList))):
    print(isPolindrome(tempList))
else:
    print(False)



