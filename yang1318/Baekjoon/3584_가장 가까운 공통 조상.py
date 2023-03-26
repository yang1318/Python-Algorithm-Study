import sys
from queue import Queue
input = sys.stdin.readline

def sap(aList, bList):
    q = Queue()
    sapLength = 100000
    sca = -1
    aVisited = [-1 for i in range(N+1)]
    bVisited = [-1 for i in range(N+1)]
    r = 1
    q.put(('a', aList[0]))
    q.put(('b', bList[0]))
    aVisited[aList[0]] = 0
    bVisited[bList[0]] = 0
    
    aDepth = 0
    bDepth = 0
    while not q.empty() :
        v = q.get()
        depth = max(aDepth, bDepth)
        if depth >= sapLength : break
        w = adj[v[1]]
        if v[0] == 'a':
            if aVisited[w] < 0:
                aVisited[w] = aVisited[v[1]] + 1
                aDepth = aVisited[v[1]] + 1
                q.put(('a', w))
                if bVisited[w] >= 0:
                    s = aVisited[w] + bVisited[w]
                    if s < sapLength :
                        sapLength = s
                        sca = w
        else :
            if bVisited[w] < 0:
                bVisited[w] = bVisited[v[1]] + 1
                bDepth = aVisited[v[1]] + 1
                q.put(('b', w))
                if aVisited[w] >= 0:
                    s = aVisited[w] + bVisited[w]
                    if s < sapLength :
                        sapLength = s
                        sca = w
    return sca
            
    
T = int(input())
for _ in range(T):
    N = int(input())
    adj = [i for i in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        adj[b] = a
    a, b = map(int, input().split())
    print(sap([a], [b]))
    