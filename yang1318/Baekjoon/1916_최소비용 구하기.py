import heapq
import sys
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def ans():
    # 입력 및 초기화
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    bus = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split()) #출발, 도착, 비용
        bus[a].append((b,c))
    start, end = map(int, sys.stdin.readline().split())

    #다익스트라 알고리즘
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        if now == end:
            print(cost)
            break
        for i in bus[now]:
            c = cost + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(q, (c, i[0]))

ans()