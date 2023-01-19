N = int(input())
M = int(input())
ans = 0
min = 10000
for i in range(N, M+1):
    if i == 1: continue
    for t in range(2, i):
        if i%t == 0: break
    else:
        ans += i
        if min > i:
            min = i
if ans == 0:
    print(-1)
else:
    print(ans)
    print(min)