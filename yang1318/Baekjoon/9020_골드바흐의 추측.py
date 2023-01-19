def isPrime(n):
    if n in prime:
        return prime[n]
    for i in range(2,n):
        if n%i == 0:
            prime[n]=False
            return False
    prime[n]=True
    return True    

T = int(input())
prime = {}
prime[1] = False

for _ in range(T):
    n = int(input())
    max = n//2 + 1 if n%2==0 else n//2 + 2
    for i in range(2,max):
        if isPrime(i) and isPrime(n-i):
            a, b = i, n-i
    print(f"{a} {b}")