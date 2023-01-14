n, m = map(int, input().split())
board = []
ans = 2500
ex1 = "WBWBWBWB"
ex2 = "BWBWBWBW"

for i in range(n):
    board.append(input())

for i in range(n-7):
    for k in range(m-7):
        tempA = 0
        tempB = 0
        for b in range(i,i+8): #8줄로 자르기
            for t in range(k, k+8): # 한줄 내에서 검사
                if b%2==0:
                    if board[b][t] != ex1[t-k]:
                        tempA += 1
                    if board[b][t] != ex2[t-k]:
                        tempB += 1
                else:
                    if board[b][t] != ex2[t-k]:
                        tempA += 1
                    if board[b][t] != ex1[t-k]:
                        tempB += 1
                temp = min(tempA, tempB)
                if temp > ans:break
        ans = min(tempA, tempB, ans)
print(ans)
