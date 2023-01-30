import sys
input = sys.stdin.readline
s = set()
for _ in range(10):
    s.add((int(input()))%42)
print(len(s))