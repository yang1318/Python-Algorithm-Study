#Backjoon 19637
#[이분탐색] IF문 좀 대신 써줘

import sys

def binary_search(arr,target):
    start=0
    end=len(arr)-1
    
    result=0
    while(start<=end):
        mid=(start+end)//2
        if(int(arr[mid][1])<target):
            start=mid+1
        else:
            result=mid
            end=mid-1
    return result        
            
    
n,k= map(int,sys.stdin.readline().split())
note=[]
power=[]
for i in range(n):
    note.append(list(map(str,sys.stdin.readline().split())))
for i in range(k):
    power.append(int(sys.stdin.readline()))
for i in range(k):
    result=binary_search(note,power[i])
    print(note[result][0])