n = int(input())
cnt = 1
ans = 1
while ans < n:
    ans = ans + cnt*6
    cnt += 1
print(cnt)