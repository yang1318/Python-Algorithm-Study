t = int(input())
for i in range(t):
    h,w,n = map(int, input().split())    
    x = n//h if n%h==0 else n//h+1
    y = n%h if n%h!=0 else h
    print(y*100+x)