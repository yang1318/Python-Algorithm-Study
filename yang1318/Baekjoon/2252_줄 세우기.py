import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v):
    if not visited[v]:
        visited[v] = True
        for i in adj[v]:
            dfs(i)
        result.append(v)

n , m = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = []
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
for i in range(1, n+1):
    dfs(i)
result.reverse()
print(*result)