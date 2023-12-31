"""
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
Предположим, что мы хотим найти элемент в массиве (получить
его индекс). Мы можем это сделать просто перебрав все элементы.
Но что, если массив уже отсортирован? В этом случае можно
использовать бинарный поиск. Принцип прост: сначала берём
элемент находящийся посередине и сравниваем с тем, который мы
хотим найти. Если центральный элемент больше нашего,
рассматриваем массив слева от центрального, а если больше -
справа и повторяем так до тех пор, пока не найдем наш элемент.

"""

x=[1,3,4,6,7,8,10,11,31]
def findIndex(xx, start, key):
    end = len(xx) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if xx[middle] == key:
            return middle
        elif xx[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
    return -1



find_element = 10
result = findIndex(x, 0, find_element)
print(result)


"""Для решения данной задачи используется процедурная и структурная парадигмы, 
так как используется формат процедуры для нахождения индекса в списке с помощью бинарного поиска,
и в процедуре присутствуют циклы и ветвления."""