triangle = sorted(list(map(int, input().split())))
while triangle[2] > 0:
    if triangle[2]**2 == triangle[0]**2 + triangle[1]**2:
        print("right")
    else:
        print("wrong")
    triangle = sorted(list(map(int, input().split())))