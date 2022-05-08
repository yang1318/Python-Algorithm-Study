import sys

# 초기화 및 입력값 받기
power_dict = {}

n,m = map(int, sys.stdin.readline().split())
for i in range(n):
    a,b = sys.stdin.readline().split()
    b = int(b)
    if b not in power_dict.keys():
        power_dict[b] = a

power_list = list(power_dict.items())
power_list.sort(key = lambda x:x[0])

# 정답 구하기 및 출력
for p in range(m):
    power = int(sys.stdin.readline()) 
    start = 0
    end = len(power_list) - 1
    result = 0
    while start <= end: #이진 탐색
        mid = (start + end) //2
        if power <= power_list[mid][0]:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(power_list[result][1])