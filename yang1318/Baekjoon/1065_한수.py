def han(x) -> bool:
    if len(x) == 1 : return True
    gap = int(x[1])-int(x[0])
    for i in range(2, len(x)):
        g = int(x[i]) - int(x[i-1])
        if not gap == g :
            return False
    return True

n = int(input())
count = 0
for i in range(1, n+1):
    if han(str(i)) : count += 1
print(count)