S=input()
count = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        count.add(S[i:j])
print(len(count))