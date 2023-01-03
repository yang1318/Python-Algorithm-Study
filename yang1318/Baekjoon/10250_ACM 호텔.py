t = int(input())
for i in range(t):
    h,w,n = map(int, input().split())
    x = str(n//h if n%h==0 else n//h+1)
    if len(x)==1 : x="0"+str(x)
    y = n%h if n%h!=0 else h
    print(f"{y}{x}")