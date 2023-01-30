import sys
input = sys.stdin.readline
C = int(input())
for _ in range(C):
    student = list(map(int, input().split()))
    aver = sum(student[1:])/student[0]
    count = 0
    for i in range(1, student[0]+1):
        if student[i] > aver:
            count += 1
    print(f"{(count/student[0])*100:.3f}%")