color1, color2 = str(input()), str(input())

if (color1.lower() == 'красный' and color2.lower() == 'синий') or (color2.lower() == 'красный' and color1.lower() == 'синий'):
    print('фиолетовый')
elif (color1.lower() == 'жёлтый' and color2.lower() == 'синий') or (color2.lower() == 'жёлтый' and color1.lower() == 'синий'):
    print('зелёный')
elif (color1.lower() == 'жёлтый' and color2.lower() == 'красный') or (color2.lower() == 'жёлтый' and color1.lower() == 'красный'):
    print('оранжевый')
else:
    print('ошибка')
