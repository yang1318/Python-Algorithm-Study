import sys 
sys.setrecursionlimit(15000)
def dfs(x,y):
    if(x<=-1 or x>=n or y<=-1 or y>=n):
        return False
    if(visited[x][y]==0):
        visited[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

graph=[]
n=int(input())
answer=0
for i in range(n):
    graph.append(list(map(int,input().split())))

# 입력받은 배열에서 가장 큰 값 , 가장 작은 값 찾기
large= max(map(max, graph))
small= min(map(min,graph))

if(large==small):
    answer=1

while(small<=large):
    result=0
    visited=[[0]*n for i in range(n)]
             
    #물에 잠기는 영역 체크
    for i in range(n):
        for j in range(n):
            if(graph[i][j]<=small):
                visited[i][j]=1
                
    #dfs를 통해 물에 잠기지 않는 영역 갯수 구하기
    for i in range(n):
        for j in range(n):
            if(dfs(i,j)==True):
                result+=1
                
    if(result>=answer):
        answer=result
    
    
    small+=1

print(answer)


    