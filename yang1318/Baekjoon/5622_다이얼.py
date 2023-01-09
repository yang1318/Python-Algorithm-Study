word = input()
dial = ['','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
for i in word:
    for k in range(len(dial)):
        if i in dial[k]:
            time += k+1
            break
print(time)