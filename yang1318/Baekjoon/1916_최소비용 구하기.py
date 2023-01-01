import heapq
import sys
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def ans():
    #입력 및 초기화
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    bus = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split()) #출발, 도착, 비용
        bus[a].append((b,c))
    start, end = map(int, sys.stdin.readline().split())
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in bus[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    print(distance[end])

ans()
