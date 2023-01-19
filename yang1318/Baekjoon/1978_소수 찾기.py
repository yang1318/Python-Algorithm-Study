N = int(input())
numList = list(map(int, input().split()))
count = N
for i in numList:
    if i <= 1:
        count -= 1
        continue
    for t in range(2, i):
        if i%t == 0: 
            count -= 1
            break
print(count)