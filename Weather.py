a = int(input('Сегодня четный день недели? '))
b = a % 2

if b == 0:
    print('Да, иди на работу.')
else:
    print('Нет, сиди дома.')
