# Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Difficulty: Easy
# Solution:

from collections import Counter

k = int(input())
roomList = Counter(map(int,input().split()))

for key,value in roomList.items():
    if(value<2):
        print(key)


