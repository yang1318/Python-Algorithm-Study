t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    for k in s:
        print(k*r,end='')
    print()