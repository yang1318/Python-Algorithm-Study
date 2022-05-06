import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    note1 = set(sys.stdin.readline().rstrip().split())
    m = int(sys.stdin.readline())
    note2 = list(sys.stdin.readline().rstrip().split())

    for x in note2:
        if x in note1:
            print(1)
        else:
            print(0)