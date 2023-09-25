hours = int(input('Введите отработанные часы: '))
kredit = int(input('Введите остаток по кредиту: '))
eat = int(input('Введите траты на еду: '))

earnings = ((200 * hours) / (2 ** 3)) + hours
balance = earnings - kredit - eat

if balance >= 0:
  print ("Можно отдохнуть.")
else:
  print ('Часов не хватает. Придётся работать больше!')
