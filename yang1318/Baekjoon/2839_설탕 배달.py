n = int(input())
if n%5==0:
    print(n//5)
else:
    cnt = 0
    ans = -1
    while cnt*5 <= n:
        if (n-(cnt * 5)) % 3 == 0 :
            ans = (n-(cnt*5))//3 + cnt
        cnt += 1
    print(ans)