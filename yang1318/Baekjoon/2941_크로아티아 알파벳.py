croatia = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}
word=input()
ans = 0
i=0
while i < len(word):
    if word[i] in croatia:
        ans += 1
        i += 1
    elif word[i:i+2] in croatia:
        ans += 1
        i += 2
    elif word[i:i+3] in croatia:
        ans += 1
        i += 3
    else:
        ans += 1
        i += 1
        
print(ans)