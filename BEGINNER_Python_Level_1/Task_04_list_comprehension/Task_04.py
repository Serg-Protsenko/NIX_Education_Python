# Дан список из строк. Создайте однострочное решение (при помощи list comprehension),
# которое приведёт к верхнему регистру все строки, содержащие слово 'price')

list_str = ['hello, world!', 'price is a very big', 'Tom Henk', 'A great price']
target_word = 'price'

list_comp_str = [i.upper() for i in list_str if target_word in i]
print(list_comp_str)
