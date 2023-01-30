import sys
input = sys.stdin.readline
s = set([i for i in range(1, 31)])
for _ in range(28):
    s.remove(int(input()))
s = sorted(list(s))
print(f"{s[0]}\n{s[1]}")