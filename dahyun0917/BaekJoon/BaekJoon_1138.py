#Backjoon 1138
#[그리디] 한 줄로 서기
n=int(input())
sl=list(map(int,input().split()))
answer=[0 for i in range(1,n+1)]
for i in range(1,n+1):
    t=sl[i-1]
    cnt=0
    for j in range(n):
        if(cnt==t and answer[j]==0):
            answer[j]=i
            break
        elif(answer[j]==0):
            cnt+=1
        
print(answer)
    
    
        
