place = int(input())

if place > 54:
    pass
elif place > 36 and place % 2 == 0:
    print('Боковое верхнее')
elif place > 36 and place % 2 != 0:
    print('Боковое нижнее')
elif place % 2 != 0:
    print('Нижнее место в купе')
elif place % 2 == 0:
    print('Верхнее место в купе')