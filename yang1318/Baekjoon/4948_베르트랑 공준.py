import sys
input = sys.stdin.readline

eratos = [True] * 246913 # 2~123456
for i in range(2, int(246912**0.5) + 1):
    if eratos[i] == True:
        j = 2
        while i*j <= 246912:
            eratos[i*j] = False
            j += 1
            
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for k in range(n+1, 2*n+1):
        if eratos[k]: count += 1
    print(count)