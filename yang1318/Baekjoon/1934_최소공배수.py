import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a, b = (b, a) if a < b else (a, b)
    m = a * b
    while b != 0:
        r = a % b
        a = b
        b = r
    print(m//a)