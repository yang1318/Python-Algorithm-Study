#Backjoon 2776
#[이분탐색] 암기왕 
import sys

def binary_search(array,target):
    start=0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    
    return 0
   
n=int(sys.stdin.readline())
for i in range(n):
    n_1=int(sys.stdin.readline())
    note1=list(map(int,sys.stdin.readline().split()))
    n_2=int(sys.stdin.readline())
    note2=list(map(int,sys.stdin.readline().split()))
    note1.sort()  
    for num in note2:
        result=binary_search(note1,num)
        if(result==1):
            print("1")
        else:
            print("0")