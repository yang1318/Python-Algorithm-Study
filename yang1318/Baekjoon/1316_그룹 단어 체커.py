n = int(input())
count = n
for i in range(n):
    word = input()
    checker = set()
    for w in range(len(word)):
        if w==len(word)-1: 
            if word[w] in checker:
                count -= 1
                break
            else:
                checker.add(word[w])
        elif word[w] != word[w+1]:
            if word[w] in checker:
                count -= 1
                break
            else:
                checker.add(word[w])
print(count)