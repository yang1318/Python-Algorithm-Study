#Code Up 3301
#[그리디] 거스름돈
money_type=[50000,10000,5000,1000,500,100,50,10]
money=int(input())
answer=0
for m in money_type:
    if(money//m>0):
        answer=answer+money//m
        money=money%m
print(answer)
