import sys
input = sys.stdin.readline
n, m = map(int, input().split())
set1 = set()
ansSet = set()
for i in range(n):
    set1.add(input().strip())
for i in range(m):
    s = input().strip()
    if s in set1:
        ansSet.add(s)
ansList = sorted(list(ansSet))
print(len(ansList))
for i in ansList:
    print(i)