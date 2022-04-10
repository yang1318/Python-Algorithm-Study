import math

n = int(input())
numbers = list(map(lambda a:int(a)%3, input().split()))
numbers.sort()
count = [0] * 3 #나머지 0, 1, 2 개 개수 세기

for i in range(n) :
  if numbers[i] == 0 :
    count[0] += 1
  elif numbers[i] == 1 :
    count[1] += 1
  else :
    count[2] += 1

ans = 0
if count[0] > 1 : #나머지가 0일 경우
  ans += math.factorial(count[0])/(math.factorial(count[0]-2)*math.factorial(2))
if count[1] > 0 and count[2] > 0 : #나머지가 1,2일 경우
  ans += count[1]*count[2]
  
print(int(ans))
