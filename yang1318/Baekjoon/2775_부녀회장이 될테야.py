n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())
    apart = [[i for i in range(1, n+1)]]
    for j in range(1, k+1):
        apart.append([])
        for m in range(n):
            apart[j].append(sum(apart[j-1][:m+1]))
    print(apart[k][n-1])