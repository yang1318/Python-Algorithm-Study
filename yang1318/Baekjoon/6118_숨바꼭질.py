from collections import deque
import sys
INF = 20001

# 입력 및 초기화
n, m = map(int, sys.stdin.readline().split())
barn = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    barn[a].append(b)
    barn[b].append(a)

visited = [INF] * (n+1)
visited[1] = 0
q = deque([1])
while q:
    v = q.popleft()
    for i in barn[v]:
        if visited[i] > visited[v] + 1: # 방문 안함
            q.append(i)
            visited[i] = visited[v] + 1
count = []
max_dist = 0
for i in range(1, n+1):
    if max_dist < visited[i]:
        max_dist = visited[i]
        count = [i]
    elif max_dist == visited[i]:
        count.append(i)

print(count[0], end=' ')
print(max_dist, end=' ')
print(len(count), end='')
    