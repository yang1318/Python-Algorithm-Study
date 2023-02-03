num = int(input())
numList = sorted(list(map(int, input().split())))
if num == 1:
    print(numList[0]**2)
else:
    print(numList[0]*numList[num-1])