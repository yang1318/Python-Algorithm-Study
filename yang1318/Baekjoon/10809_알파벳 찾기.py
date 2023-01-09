s = input()
ans = [-1]*26
for i in range(len(s)):
    if ans[ord(s[i])-97] < 0:
        ans[ord(s[i])-97]=i
for i in ans:
    print(i, end=' ')