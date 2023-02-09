#BackJoon 4948 베르트와 공준
import sys
import math

def sieve_of_Eratosthenes(n):  # 에라토스테네스의 체 구현 함수
    graph=[True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if graph[i]==True:
            j=2
            while i*j<=n:
                graph[i*j]=False
                j+=1
    return graph

list=[]    

# 모든 입력 값을 list에 저장
while True:   
    n = int(sys.stdin.readline())
    if n==0 : break
    list.append(n)

# 입력받은 수 중 가장 큰 수 * 2를 인자로 함수 호출
graph=sieve_of_Eratosthenes(max(list)*2)  

for i in list: 
    count=0
    for j in range(i+1,i*2+1): # 입력받은 수 ~ 입력받은 수 * 2
        if graph[j] : count+=1 # graph의 값이 True ( 소수 )면 count 증가
    print(count)
