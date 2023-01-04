n, m = map(int, input().split())
card = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            s = card[i]+card[j]+card[k]
            if s<=m:
                if ans<s:
                    ans=s
                break
print(ans)