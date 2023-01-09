s = input().upper()
dict = {}
for i in s:
    if i in dict:
        dict[i] += 1
    else : dict[i] = 1
ans = ""
maxValue = max(dict.values())
for k, v in dict.items():
    if v==maxValue :
        if ans != "" :
            ans = "?"
            break
        else :
            check = True
            ans = k
print(ans)