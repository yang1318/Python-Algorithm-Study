import sys

# 입력 및 초기화
n = int(sys.stdin.readline())
student = []
for i in range(n):
    student.append(sys.stdin.readline().split())
    student[i][1] = int(student[i][1])
    student[i][2] = int(student[i][2])
    student[i][3] = int(student[i][3])

#정렬
student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 출력
for i in range(n):
    print(student[i][0])
