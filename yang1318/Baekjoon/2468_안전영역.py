from collections import deque
import sys

# 입력 및 초기화
n = int(sys.stdin.readline())
slope = []
min_slope = 1
max_slope = 1
for i in range(n):
    slope.append(list(map(int, sys.stdin.readline().split())))
    max_slope = max(slope[i]) if max_slope < max(slope[i]) else max_slope
    min_slope = max(slope[i]) if min_slope > max(slope[i]) else min_slope

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    if graph[x][y] == 1:
        return False
    # graph[x][y] == 0 일때
    q = deque()
    q.append((x, y))
    graph[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
    return True


graph = [[] for _ in range(n)]
ans = 1
for i in range(min_slope, max_slope):
    for j in range(n):  # 비의 양에 따른 그래프 만들기
        graph[j] = list(map(lambda a: 1 if a <= i else 0, slope[j]))

    result = 0
    for k in range(n):
        for m in range(n):
            if bfs(k, m):
                result += 1
    if ans < result:
        ans = result

print(ans)