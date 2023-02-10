import sys
input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().split()))
k = int(input())
p, q = 0, 0
count = 0
nSum = nList[0]

while p<=q and q<n:
    if nSum > k:
        count += n-q
        p += 1
        q = p
        nSum = nList[p]
    else:
        if q+1>=n:
            break
        q += 1
        nSum += nList[q]
print(count)