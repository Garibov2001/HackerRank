# Link: https://www.hackerrank.com/challenges/the-minion-game/problem
# Difficulty: Medium
# Solution:

def minion_game(string):
    myVowelSet= {"A","E","I","O","U"}

    firstScore = 0
    secondScore = 0
    stringLength = len(string)

    for k in range(0, stringLength):
        if(string[k] not in myVowelSet):
            firstScore += (stringLength-k)
        else:
            secondScore += (stringLength-k)

    if(firstScore > secondScore):
        print(f'Stuart {firstScore}')
    else:
        if(firstScore < secondScore):
            print(f'Kevin {secondScore}')
        else:
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)