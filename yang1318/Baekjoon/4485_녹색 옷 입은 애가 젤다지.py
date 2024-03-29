import heapq
import sys
INF = int(1e9)

# 정답 구하기
def ans_dijkstra(n):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (cave[0][0], (0,0)))
    distance = [[INF]*n for _ in range(n)]
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now[0]][now[1]] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            if 0 <= x <= n-1 and 0 <= y <= n-1:
                cost = dist + cave[x][y]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[x][y]:
                    distance[x][y] = cost
                    heapq.heappush(q, (cost, (x,y)))
    return distance[n-1][n-1]

# 입력 및 초기화
problem_num = 1
while(True): 
    cave = []
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(n):
        cave.append(list(map(int, sys.stdin.readline().split())))
    ans = ans_dijkstra(n)
    print("Problem " + str(problem_num) + ": " + str(ans))
    problem_num += 1
