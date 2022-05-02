import sys

# 입력 및 초기화
n = int(sys.stdin.readline())
student = []
for i in range(n):
    name, a, b, c = sys.stdin.readline().split()
    a, b, c = int(a), int(b), int(c)
    student.append([-a, b, -c, name])

#정렬
student.sort()

# 출력
for i in range(n):
    print(student[i][3])
