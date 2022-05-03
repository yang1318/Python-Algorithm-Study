#Backjoon 1389
#[dfs/bfs] 케빈 베이컨의 6단계 법칙
import sys
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] += visited[v] + 1
#변수 초기화
n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]

#입력받기
for i in range(m) : 
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

#정답 구하기
min = 5001
for i in range(1,n+1):
    visited = [0] * (n+1)
    bfs(graph, i, visited)
    kevin = sum(visited) - 1
    if kevin < min:
        min = kevin
        ans = i
print(ans)