year = int(input())

if (year % 4 == 0 or year % 100 != 0) or year % 100 != 0:
    print(f'{year} год високосный')
else:
    print(f'{year} год не високосный')