N = int(input())
card1 = list(input().split())
M = int(input())
card2 = list(input().split())
count = {}
for i in card1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i in card2:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')