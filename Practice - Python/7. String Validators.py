# Link: https://www.hackerrank.com/challenges/string-validators/problem
# Difficulty: Easy
# Solution:

if __name__ == '__main__':
    myString = input()
    for i in range(0, len(myString)):
        if(myString[i].isalnum()):
            print(True)
            break
    else:
        print(False)
        
    for i in range(0, len(myString)):
        if(myString[i].isalpha()):
            print(True)
            break
    else:
        print(False)

    for i in range(0, len(myString)):
        if(myString[i].isdigit()):
            print(True)
            break
    else:
        print(False)
        
    for i in range(0, len(myString)):
        if(myString[i].islower()):
            print(True)
            break
    else:
        print(False)

    for i in range(0, len(myString)):
        if(myString[i].isupper()):
            print(True)
            break
    else:
        print(False)



