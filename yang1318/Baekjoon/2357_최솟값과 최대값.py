# 50524KB / 2648ms
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
limit = 1000000001
arr = [0]
tree = [(limit, 0)]*(n*4)
for _ in range(n):
    i = int(input())
    arr.append(i)

# node가 담당하는 구간 [start, end]
def treeInit(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return tree[node]
    else:
        left = treeInit(node*2, start, (start+end)//2)
        right = treeInit(node*2+1, (start+end)//2+1, end)
        tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
        return tree[node]

# node가 담당하는 구간 [start, end]
# 최소/최대값을 구해야하는 구간 [left, right]
def query(node, start, end, left, right) :   
    if left > end or right < start :
        return (limit, 0)

    if left <= start and end <= right :
        return tree[node]

    leftNode = query(node*2, start, (start+end)//2, left, right)
    rightNode = query(node*2 + 1, (start+end)//2+1, end, left, right)
    return (min(leftNode[0], rightNode[0]), max(leftNode[1], rightNode[1]))

treeInit(1, 1, n)
for _ in range(m):
    a, b = map(int, input().split())
    print(*query(1, 1, n, a, b))