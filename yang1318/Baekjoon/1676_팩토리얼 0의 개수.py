import math
nf = math.factorial(int(input()))
snf = str(nf)
count = 0
for i in range(len(snf)-1, -1, -1):
    if snf[i] == "0":
        count += 1
    else:
        print(count)
        break