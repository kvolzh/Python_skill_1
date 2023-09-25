tovar_1 = int(input('Введите стоимость первого товара: '))
tovar_2 = int(input('Введите стоимость первого товара: '))
tovar_3 = int(input('Введите стоимость первого товара: '))

summa = tovar_1 + tovar_2 + tovar_3

print ('Сумма чека:', summa)

if summa > 10000:
  summa_skidka = summa * 10 / 100
  final_summa = summa - summa_skidka
  print ('Итоговая сумма:', final_summa)
else:
  print ('Калькулятор скидки не нужен')