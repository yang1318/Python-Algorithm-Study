x = int(input())
count = 1
add = 2
while True:
    if x <= count :
        if add%2 == 0:
            print(count-x+1,end='/')
            print(add-count+x-1)
        else:
            print(add-count+x-1,end='/')
            print(count-x+1)
        break
    count += add
    add += 1