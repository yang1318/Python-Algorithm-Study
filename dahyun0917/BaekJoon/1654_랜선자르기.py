#Backjoon 1654
#[이분탐색] 랜선자르기
import sys
k,n=map(int,sys.stdin.readline().split())
ren=[0 for i in range(k)]
for i in range(k):
    ren[i]=(int(sys.stdin.readline()))

start=0
end=max(ren)

result=1
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in ren:
        if(x>=mid and mid>0):
            total+=x//mid
    if total<n:
        end=mid-1
    else:
        result=mid
        start=mid+1
        
        
print(result)