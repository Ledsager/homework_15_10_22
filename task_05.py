# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from cmath import sqrt


n = int(input('Задайте число для формирования ряда Фибоначчи (n>2): '))
fib = [0]
prev_fib1, prev_fib5 = 0, 0
next_fib2, next_fib6 = 1, 1
if n >= 2:
    for i in range(0, n):

        next_fib2 = prev_fib1+next_fib2
        prev_fib1 = next_fib2-prev_fib1
        next_fib6 = prev_fib5-next_fib6
        prev_fib5 = prev_fib5-next_fib6
        fib.append(prev_fib1)
        fib.insert(0, prev_fib5)
    print(fib)
else:
    print('Введено не верное значение!')


# попытка через формулу Бине (прямой список формируется, алгоритм для обратного списка
# только если через один шаг умножать на -1 - не реализовал т.к. считаю не верным подходом)
# i=0
# while i <= n:
#     sq5 = sqrt(5)
#     a = (1 + sq5) / 2
#     b = (1 - sq5) / 2
#     next_fib2 = (pow(a, i) - pow(b, i)) / sq5
#     # prev_fib1=int(next_fib2)
#     i += 1
#     print(' ', next_fib2, end=' ,')
