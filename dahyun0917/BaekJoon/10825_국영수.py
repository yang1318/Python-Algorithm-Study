#Backjoon 10825
#[정렬] 국영수
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))

arr=sorted(arr,key=lambda x:x[0])
arr=sorted(arr,key=lambda x:-int(x[3]))
arr=sorted(arr,key=lambda x:int(x[2]))
arr=sorted(arr,key=lambda x:-int(x[1]))

for i in range(n):
    print(arr[i][0],end='\n')