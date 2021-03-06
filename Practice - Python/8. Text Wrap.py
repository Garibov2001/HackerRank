# Link: https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen
# Difficulty: Easy
# Solution:

import textwrap

def wrap(string, max_width):
    returnString = ""
    nextString = string[0]
    paragraph = 0
    for i in range(1, len(string)):
        if (paragraph < max_width - 1):
            nextString = nextString + string[i]
            paragraph += 1
        else:
            returnString += nextString + "\n"
            paragraph = 0
            nextString = string[i]
    returnString += nextString
    return returnString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)