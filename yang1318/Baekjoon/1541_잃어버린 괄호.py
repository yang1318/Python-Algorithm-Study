formula = input()

ans = 0
add = True
number = ''

for i in formula :
  if i == '+' :
    if add :
      ans += int(number)
    else :
      ans -= int(number)
    number = ''
  elif i == '-' :
    if add :
      ans += int(number)
    else :
      ans -= int(number)
    add = False
    number = ''
  else :
    number += i
    
if add :
  ans += int(number)
else :
  ans -= int(number)
print(ans)
