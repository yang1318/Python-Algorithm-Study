#Baeckjoon 1541 
#[그리디] 잃어버린 괄호
expression=[]
answer=0
expression=input().split('-')
for i in range(len(expression)):
    plus_ex=[]
    sum=0
    plus_ex=expression[i].split('+')
    for j in range(len(plus_ex)):
        sum+=int(plus_ex[j])
    if(i!=0):
        answer-=sum
    else:
        answer=sum
print(answer)

