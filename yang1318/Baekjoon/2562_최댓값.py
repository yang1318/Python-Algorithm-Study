import sys
input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]
max, maxIndex = 0, 0
for i in range(9):
    if arr[i] > max:
        max, maxIndex = arr[i], i
print(f"{max}\n{maxIndex+1}")