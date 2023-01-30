N = int(input())
score = list(map(int, input().split()))
M = max(score)
ans = 0
for i in range(N):
    ans += score[i]/M*100
print(ans/N)