n = int(input())
people = []
rank = [1]*n
for i in range(n):
    x, y = map(int, input().split())
    people.append((x,y))
    for k in range(len(people)):
        if people[k][0] < x and people[k][1] < y:
            rank[k] += 1
        if people[k][0] > x and people[k][1] > y:
            rank[len(people)-1] += 1
for i in rank:
    print(i, end=' ')