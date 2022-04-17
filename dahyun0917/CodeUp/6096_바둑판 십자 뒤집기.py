#Code up 6096
#[기초-종합] 바둑판 십자 뒤집기
#d=[[0]for j in range(19)]
#for i in range(19):
#    d[i]=(list(map(int,input().split())))

d = [list(map(int, input().split())) for _ in range(19)]
n=input()

for i in range(int(n)):
    x,y= input().split()
    for j in range(19):
        if(d[int(x)-1][j]==0):
            d[int(x)-1][j]=1
        else:
            d[int(x)-1][j]=0
        if(d[j][int(y)-1]==0):
            d[j][int(y)-1]=1
        else:
            d[j][int(y)-1]=0

for i in range(19):
    for j in range(19):
        print(d[i][j],end=' ')
    print()
    
