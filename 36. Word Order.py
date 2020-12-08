# Link: https://www.hackerrank.com/challenges/word-order/problem
# Difficulty: Medium
# Solution:

from collections import Counter

numberWords = int(input())


words = []

for i in range(0, numberWords):
    words.append(input())

print(len(set(words)))  #length of the set unique words

for key,value in Counter(words).items():
    print(value,end=" ")


