n = int(input())
ans = []
list = list(map(int, input().split()))

for i in range(n-1, -1, -1) :
  ans.insert(list[i],str(i+1))

print(' '.join(ans))
