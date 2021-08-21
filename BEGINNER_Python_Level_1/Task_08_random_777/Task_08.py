# Есть список из случайных чисел и строк. Создайте цикл, итерирующийся до тех пор, пока не встретится
# число "777". Если в течении 100 попыток число не будет найдено — остановить цикл и вызвать ошибку с
# соответсвующим сообщением.

random_list_01 = ['one', 22, 'twenty three', 5, 777]
random_list_02 = [ 'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9,
                   'one', 22, 'twenty three', 5, 'Ivan', 6, 'five', 7, 'six', 9, 101]

required_number = 777
lst = random_list_01

i = 0
for item in lst:
    if str(required_number) in str(item):
        print(f'Find the required number {required_number} in this list with a position: {lst.index(item)}')
        break
    if i == 99:
        print('We had 100 attempts and no number was found!')
        break
    i += 1

lst = random_list_02
n = 0
while n <= 100:
    if str(required_number) in str(lst[n]):
        print(f'Find the required number {required_number} in this list with a position: {lst.index(lst[n])}')
        break
    n += 1
else:
    print('We had 100 attempts and no number was found!')
