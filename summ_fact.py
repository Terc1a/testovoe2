num = int(input())           # кол-во факториалов
total = 0                    # сумма факториалов
factorial = 1               # вычисляемый факториал

for i in range(1, num+1):    # перебираем факториалы
    for j in range(1, i+1):  # вычисляем каждый факториал
        factorial *= j       # вычисляем факториал
    total += factorial       # Суммируем факториалы чисел.
    factorial = 1            # "обнуляем факториал"
print(total)