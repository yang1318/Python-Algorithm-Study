#Backjoon 6236
#[이분탐색] 용돈관리
import sys

n,m=map(int,sys.stdin.readline().split())
money=[]
for i in range(n):
    money.append(int(sys.stdin.readline()))

start=0
end=max(money)

result=1
while(start<=end):
    total=0
    mid=(start+end)//2
    
    for m in money:
        if(mid<m):
            total+=1
            
    if(total<=m):
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)