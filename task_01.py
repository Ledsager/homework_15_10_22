# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def input_mas():
    mas = []
    mas = [int(i) for i in input().split()]
    return mas


def summa_even_element(list_a):
    sum = 0
    for i in range(0, len(list_a)-1):
        if ((i+1) % 2) == 0:
            sum = sum + int(list_a[i])
            print(list_a[i])
    return sum


print('Введите массив переменных : ')
list_a = input_mas()
print(list_a)
print(f'Сумма элементов на четных позициях = {summa_even_element(list_a)} ')
