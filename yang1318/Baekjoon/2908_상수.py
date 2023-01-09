a,b = input().split()
a, b = int(''.join(reversed(a))), int(''.join(reversed(b)))
if int(a) > int(b) : print(a)
else : print(b)