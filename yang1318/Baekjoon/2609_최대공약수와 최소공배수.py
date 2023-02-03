a, b = map(int, input().split())
a1, b1 = (b, a) if a < b else (a, b)
while b1 != 0:
    r = a1 % b1
    a1 = b1
    b1 = r
s = a1 * (b//a1) * (a//a1)
print(a1, s)