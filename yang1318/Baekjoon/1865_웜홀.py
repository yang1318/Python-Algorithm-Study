import sys
input = sys.stdin.readline
INF = int(1e9)

def bf():
    # 전체 n - 1번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(2*m+w):
            cur_node = adj[j][0] # 출발지
            next_node = adj[j][1] # 도착지
            edge_cost = adj[j][2] # 비용
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False
TC = int(input())
for _ in range(TC):
    n, m, w = map(int, input().split())
    adj = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        adj.append((s, e, t))
        adj.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        adj.append((s, e, -t))
    distance = [INF] * (n + 1)
    if bf():
        print("YES")
    else:
        print("NO")
    # for i in range(1, n+1):
    #     distance = [INF] * (n + 1)
    #     if bf(i):
    #         print("YES")
    #         break
    # else:
    #     print("NO")