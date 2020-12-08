# Link: https://www.hackerrank.com/challenges/calendar-module/problem
# Difficulty: Easy
# Solution: 

import calendar

## MM DD YYYY
enterDate = list(map(int, input().split()))

day = calendar.weekday(enterDate[2], enterDate[0], enterDate[1])
print (calendar.day_name[day].upper())