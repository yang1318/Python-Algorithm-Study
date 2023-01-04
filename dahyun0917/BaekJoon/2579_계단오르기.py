#Backjoon 2579
#[동적계획법] 계단오르기

import sys

n=int(sys.stdin.readline())
dp=[0]*100000
stair=[0]*100000
for i in range(1,n+1):
    stair[i]=int(sys.stdin.readline())
    
dp[1]=stair[1]
dp[2]=stair[2]+stair[1]

for i in range(3,n+1):
    #print(i,"일때 ",i-2,":",dp[i-2]+dp[i],",",i-1,':',dp[i-1]+dp[i])
    dp[i]=max(dp[i-2]+stair[i],stair[i-1]+stair[i]+dp[i-3])
           
print(dp[n])
