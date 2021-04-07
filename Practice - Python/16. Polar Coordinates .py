# Link: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Difficulty: Easy
# Solution: 

from cmath import phase

myComplex = input()

print(abs(complex(myComplex)))
print(phase(complex(myComplex)))