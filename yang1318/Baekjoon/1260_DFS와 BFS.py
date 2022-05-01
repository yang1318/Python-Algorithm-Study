import sys
from collections import deque

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n,m,v = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]

for i in range(m) :
  a, b = map(int, sys.stdin.readline().strip().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()

visited1 = [False] * (n+1)
dfs(graph, v, visited1)
print()
visited2 = [False] * (n+1)
bfs(graph, v, visited2)