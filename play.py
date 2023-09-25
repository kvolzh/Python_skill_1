kk = int(input('Кубик кости: '))
kv = int(input('Кубик владельца: '))

if kk >= kv:
  razn = kk - kv
  print (razn)
  print ('Игрок платит')
else:
  razn = kk + kv
  print (razn)
  print ('Владелец платит')
print ('Игра окончена')
