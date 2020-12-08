# Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# Difficulty: Easy
# Solution:

from __future__ import division

def average(array):
    mySet = set(arr)

    return sum(mySet)/ len(mySet)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = average(arr)
    print (result)