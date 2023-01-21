K = int(input())
arr = [0, 0, 0, 0, 0, 0]
w, h = 0, 0
wIdx, hIdx = -1, -1
for i in range(6):
    arr[i] = list(map(int, input().split()))
    if arr[i][0]==1 or arr[i][0]==2:
        if w < arr[i][1]:
            w = arr[i][1]
            wIdx = i
    else:
        if h<arr[i][1]:
            h = arr[i][1]
            hIdx = i
subW = abs(arr[(wIdx-1)%6][1]-arr[(wIdx+1)%6][1])
subH = abs(arr[(hIdx-1)%6][1]-arr[(hIdx+1)%6][1])
ans = K*(w*h-subW*subH)
print(ans)