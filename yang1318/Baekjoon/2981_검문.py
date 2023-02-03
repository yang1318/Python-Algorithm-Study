import sys
input = sys.stdin.readline
nCount = int(input())
nList = [int(input()) for _ in range(nCount)]

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

nList.sort()
newList = [nList[i]-nList[i-1] for i in range(1, nCount)]
if nCount == 2:
    m = newList[0]
else:
    m = gcd(newList[0], newList[1])
    for i in range(2, len(newList)):
        m = gcd(m, newList[i])

result = set()
for i in range(2, int(m**0.5)+1):
    if m % i == 0:
        result.add(i)
        result.add(m//i)
result.add(m)
print(*sorted(list(result)))