numOfA, numOfB = map(int, input().split())
A, B = set(map(int, input().split())), set(map(int, input().split()))
print(numOfA+numOfB-2*len(A&B))