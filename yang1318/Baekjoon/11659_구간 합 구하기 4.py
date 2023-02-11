import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nList = list(map(int, input().split()))
addList = [0] * n
addList[0] = nList[0]
for k in range(1, n):
    addList[k] = addList[k-1]+nList[k]
for _ in range(m):
    i, j = map(int, input().split())
    if i==1: print(addList[j-1])
    else: print(addList[j-1]-addList[i-2])