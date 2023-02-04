import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    d = dict()
    for _ in range(n):
        name, category = input().split()
        if category in d:
            d[category] += 1
        else:
            d[category] = 1
    ans = 1
    for value in d.values():
        ans *= value + 1
    print(ans-1)