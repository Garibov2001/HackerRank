# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Difficulty: Easy
# Solution:

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key, value in student_marks.items():
        if(key == query_name):
            x = sum(value)/3
            print('%.2f'%x)
