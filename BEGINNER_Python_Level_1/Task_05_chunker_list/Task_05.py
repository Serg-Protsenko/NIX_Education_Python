# Напишите функцию, которая принимает список, и число. Функция должна разбить список на N кусков,
# переданных в функцию в качестве втрого аргумента. Выполнить проверки по здравому смыслу
# (например, нет смысла пытаться разбить список из 3 элементов на 4 элемента)

def chunker_list(list_name, n):
    if n > len(list_name):
        return 'Sorry, but your list is a too short for this size of the chunk'
    elif n == 1:
        return list_name
    elif n <= 0:
        return 'Attention! Your size of chunk must be great than 0! '
    return [list_name[i::n] for i in range(n)]

lst = list(range(22))
n = 1
print(chunker_list(lst, n))

n = -1
print(chunker_list(lst, n))

n = 2
print(chunker_list(lst, n))

n = 24
print(chunker_list(lst, n))
