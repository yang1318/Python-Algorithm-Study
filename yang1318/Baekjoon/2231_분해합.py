n = int(input())
m = 0
sum = 0
while m < n and sum != n:
    m += 1
    sum = m
    for i in str(m):
        sum += int(i)
if sum == n:
    print(m)
else:
    print("0")