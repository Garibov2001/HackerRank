# Link: https://www.hackerrank.com/challenges/itertools-product/problem
# Difficulty: Easy
# Solution:

from itertools import product

A = input().split(" ")

B = input().split(" ")


for aElement in A:
    for bElement in B:
        print(f'({aElement}, {bElement})', end=" ")