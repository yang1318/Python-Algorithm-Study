#Backjoon 4485
#[다익스트라] 녹색 옷 입은 애가 젤다지?

import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dijkstra(cave,n):
    q=[]
    distance=[[INF]*n for i in range(n)]
    heapq.heappush(q,(cave[0][0],0,0))
    while q:
        dist,row,col=heapq.heappop(q)
        if distance[row][col] < dist:
            continue
        for i in range(4):
            ny=row+dy[i]
            nx=col+dx[i]
            if nx>=0 and ny>=0 and nx<n and ny<n:
                cost=dist+cave[ny][nx]
                if cost<distance[ny][nx]:
                    distance[ny][nx]=cost
                    heapq.heappush(q,(cost,ny,nx))
    return distance[n-1][n-1]
num=1
while(True):
    n=int(input())
    if(n==0):
        break
    cave=[]
    for i in range(n):
        cave.append(list(map(int,input().split())))
    
    result=(dijkstra(cave,n))
    print("Problem "+str(num)+": "+str(result)) 
    num+=1  

    