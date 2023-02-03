def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

n = int(input())
ring = list(map(int, input().split()))
for i in range(1, n):
    r = gcd(ring[0], ring[i])
    print(f"{ring[0]//r}/{ring[i]//r}")