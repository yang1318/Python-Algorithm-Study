import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input()
    score = 0
    count = 0
    for i in s:
        if i == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)