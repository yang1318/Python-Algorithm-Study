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
