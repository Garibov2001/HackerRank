# Link: https://www.hackerrank.com/challenges/python-string-formatting/problem?h_r=next-challenge&h_v=zen
# Difficulty: Easy
# Solution:

def print_formatted(number):
    
    length = len(str(bin(number))[2:]) + 1 
    for i in range(1, number +1):
        print(str(i).rjust(length-1),end= "")
        print(str(oct(i))[2:].rjust(length), end= "")
        print(str(hex(i))[2:].upper().rjust(length), end= "")
        print(str(bin(i))[2:].rjust(length), end= "")
        print()
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)