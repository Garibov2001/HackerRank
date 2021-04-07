# Link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# Difficulty: Medium
# Solution:


# 1) It must start with a 4, 5 or 6.
def StartWith(argString):
    if(argString[0] == "4" or
       argString[0] == "5" or
       argString[0] == "6"):
       return True
    else:
        return False

# 2) It must contain exactly 16 digits.
# 4) It may have digits in groups of 4, separated by one hyphen "-"
def ContainDigit(argString):
    myLength = 0
    if("-" in argString):
        if(len(argString) == 19):
            argString = argString.split("-")
            if(not(len(argString[0]) == 4 and len(argString[1]) == 4 and len(argString[2]) == 4 and len(argString[3]) == 4)):
                return False
            argString = argString[0] + argString[1] + argString[2] + argString[3]
            myLength = len(argString)
        else:
            return False
    else:
        myLength = len(argString)
    return myLength == 16

# 3) It must only consist of digits (0-9)
# 5) It must NOT use any other separator like ' ' , '_', etc.
def isValidForm(argString):
    for element in argString:
        if(not (element == "-" or (ord(element)>=48 and ord(element)<=57))):
            return False
    return True

# 6) It must NOT have 4 or more consecutive repeated digits.
def NotConsecutive(argString):
    counter = 1
    if("-" in argString):
        argString = argString.split("-")
        argString = argString[0] + argString[1] + argString[2] + argString[3]
        
    for i in range(0, len(argString)):
        if( i!= len(argString) - 1 and argString[i] == argString[i + 1]):
            counter += 1 
        else:
            if(counter >= 4 ):
                return False            
            counter = 1
    return True


numCard = int(input())


for i in range(0, numCard):
    text = input()
    
    if(all( [StartWith(text), isValidForm(text), ContainDigit(text), NotConsecutive(text)] )):
        print("Valid")
    else:
        print("Invalid")




