#Baeckjoon 1931
#[그리디] 회의실 배정

#시간초과
n=int(input())
answer=0
mr=[list(map(int,input().split())) for i in range(n)]
mr.sort()

for i in range(n):
    if(mr[n-1][0]-mr[i][0]<answer or (n-1)-i<answer):
        break
    sum=1
    end=mr[i][1]
    for j in range(i+1,n):
        if(end<=mr[j][0]):
            sum+=1
            end=mr[j][1]
    
    if(answer<sum):
        answer=sum
print(answer)

#시간초과나지 않는 코드
n = int(input())
list = [list(map(int, input().split())) for _ in range(n)]

list.sort(key = lambda x: x[0])
list.sort(key = lambda x: x[1])
 
min = list[0][1]
count = 1

for i in range(1,n) :
  if list[i][0] >= min :
    min = list[i][1]
    count += 1

print(count)

