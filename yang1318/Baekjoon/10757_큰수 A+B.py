a,b = input().split()
ans = ""
carry = False
ai, bi=len(a)-1, len(b)-1

while ai>=0 or bi>=0:
    if ai<0:
        b1 = int(b[bi])
        next = b1+1 if carry else b1
        carry=True if next>=10 else False
        ans = str(next%10)+ans
        bi = bi-1
    elif bi<0:
        a1 = int(a[ai])
        next = a1+1 if carry else a1
        carry=True if next>=10 else False
        ans = str(next%10)+ans
        ai = ai-1
    else :
        a1, b1 = int(a[ai]), int(b[bi])
        next = a1+b1+1 if carry else a1+b1
        carry=True if next>=10 else False
        ans = str(next%10) + ans
        ai, bi = ai-1, bi-1
if carry : ans="1"+ans
print(ans)