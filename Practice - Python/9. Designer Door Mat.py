# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
# Difficulty: Easy
# Solution:


myString = input()
details = myString.split(" ")

N = int(details[0])

for i in range(1, N//2 +1, 1):
    for j in range(N//2 + 1, i, -1):
        print("---", end="")
    for k in range(0, 2*i-1):
        print(".|.",  end="")
    for j in range(N//2 +1, i, -1):
        print("---", end="")
    print()
print("WELCOME".center(3*N,"-"))

for i in range(N//2 +1, 1, -1):
    for j in range(N//2 +1, i-1, -1):
        print("---", end="")
    for k in range(2*i-1, 2, -1):
        print(".|.",  end="")
    for j in range(N//2 +1, i-1, -1):
        print("---", end="")
    print()




