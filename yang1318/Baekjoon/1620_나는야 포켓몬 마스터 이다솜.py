import sys
# 다솜아 이걸로 도감을 꼭 얻어서 진정한 포켓몬 마스터가 되렴!!!
input = sys.stdin.readline
n, m = map(int, input().split())
numDogam = {}
alphaDogam = {}
for i in range(1, n+1):
    name = input().strip()
    numDogam[i] = name
    alphaDogam[name] = i
for i in range(m):
    quiz = input().strip()
    if quiz in alphaDogam:
        print(alphaDogam[quiz])
    else:
        print(numDogam[int(quiz)])