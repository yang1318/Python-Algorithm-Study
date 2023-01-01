import sys
import heapq
INF = int(1e9)

# 입력 및 초기화
v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
for i in range(e):
    u, b, w = map(int, sys.stdin.readline().split())
    graph[u].append((b, w))

# 다익스트라
q = []
distance = [INF] * (v+1)
distance[start] = 0
heapq.heappush(q, (0, start))
while q:
    cost, now = heapq.heappop(q)
    if cost > distance[now]:
        continue
    for i in graph[now]:
        c = cost + i[1]
        if c < distance[i[0]]:
            distance[i[0]] = c
            heapq.heappush(q, (c, i[0]))
            
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

