def d(n: str) -> int :
    sum = int(n)
    while len(n) > 0 :
        sum = sum + int(n[-1])
        n = n[:-1]
    return sum

if __name__ == "__main__" :
    a = [False] * 10001
    for i in range(10001) :
        s = d(str(i))
        if s <= 10000 :
            a[s] = True
    for i in range(10001) :
        if not a[i] : print(i)