board = [[0]*19 for _ in range(19)]

for i in range(19):
  board[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
  x, y = map(lambda a:int(a)-1, input().split())
  for k in range(19):
    if k==x:
      continue
    if board[k][y] == 1:
      board[k][y] = 0
    else:
      board[k][y] = 1
  for j in range(19):
    if j==y:
      continue
    if board[x][j] == 1:
      board[x][j] = 0
    else:
      board[x][j] = 1

for i in range(19):
  for j in range(19):
    print(board[i][j], end=' ')
  print()
