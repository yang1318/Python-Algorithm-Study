import sys

# 입력 및 초기화
k, n = map(int, sys.stdin.readline().split())
lan = []
for i in range(k):
    lan.append(int(sys.stdin.readline()))

start = 1
end = max(lan)
result = 0
while start <= end: # 이진 탐색
    mid = (start + end) // 2
    total = 0
    for i in range(k):
        total += lan[i] // mid
    if total >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)