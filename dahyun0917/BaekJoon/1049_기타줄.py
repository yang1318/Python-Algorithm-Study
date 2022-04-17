#Backjoon 1049
#[그리디] 기타줄
answer=0
n,m=map(int,input().split())
set=[0 for i in range(m)]
piece=[0 for i in range(m)]
for i in range(m):
    set[i],piece[i]=map(int,input().split())

if(n//6>0):
    if(min(piece)*6*(n//6)<min(set)*(n//6)):
        answer+=min(piece)*6*(n//6)
    else:
        answer+=(min(set))*(n//6)
    n=n%6
if(n>0):
    if(min(piece)*n<min(set)):
        answer+=min(piece)*n
    else:
        answer+=min(set)
print(answer)
