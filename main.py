a=int(input('Введите цифру обозначающую день недели:'))

if a>7 or a<1:
    print('Цифра несоответствует дню недели')
elif a==6 or a==7:
    print('Да')
else:
    print('Нет')