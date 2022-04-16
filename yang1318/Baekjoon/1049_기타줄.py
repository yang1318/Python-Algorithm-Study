n, m = map(int, input().split())
min_package, min_piece = 1001, 1000

for i in range(m) :
  package, piece = map(int, input().split())
  if(min_package > package) :
    min_package = package
  if(min_piece > piece) :
    min_piece = piece

min1 = min_piece * n #낱개만
min2 = min_package * (n//6 + 1 if n%6 > 0 else n//6) #패키지만
min3 = min_package * (n//6) + min_piece * (n%6) #패키지 + 낱개

print(min(min1, min2, min3))
