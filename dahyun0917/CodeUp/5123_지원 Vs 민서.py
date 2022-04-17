#Code Up 5123
#[탐색기반설계] 지원 vs 민서(small)
import math
n=int(input())
age_list=list(map(int,input().split()))
answer=0
# for i in range(n):
#     for j in range(i+1,n):
#         if((age_list[i]+age_list[j])%3==0):
#             answer+=1
         
count=[0]*3
   
for age in age_list:
    if(age%3==0):
        count[2]+=1
    elif(age%3==1):
        count[0]+=1
    elif(age%3==2):
        count[1]+=1
print(count[0],count[1],count[2])

if(count[0]>0 and count[1]>0):
    answer+=(count[0]*count[1])
if(count[2]>0):
    answer+=(math.factorial(count[2])//((math.factorial(count[2]-2))*math.factorial(2)))


print(answer)
