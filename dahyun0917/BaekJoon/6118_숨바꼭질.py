#Backjoon 6118
#[다익스트라] 숨바꼭질 
import heapq
import sys
INF = int(1e9)

n,m = map(int,sys.stdin.readline().split())
graph =[[]for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+1
            if cost<distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))

dijkstra(1)
max=0
num=0
sd=0
for i in range(1,n+1):
    if distance[i] > max:
        max=distance[i]
        num=i
        sd=0
    if max==distance[i]:
        sd+=1
print(num,max,sd)
        
            


