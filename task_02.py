# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def input_mas():
    mas = []
    mas = [int(i) for i in input().split()]
    return mas


def multiply_element(list_a):
    multiply_mas = []
    
    if len(list_a)%2==0:
        len_list_a=int(len(list_a)/2)
    else:
        len_list_a=int(len(list_a)/2)+1
    # print(len_list_a,len(list_a))
    for i in range(0,len_list_a):
        temp=list_a[i]*list_a[-i-1]
        multiply_mas.append(temp)
        print(f'{list_a[i]} - {list_a[-i-1]}')
    return multiply_mas


print('Введите массив переменных : ')
list_a = input_mas()
print(list_a)
print(f'Результирующий массив: {multiply_element(list_a)} ')
