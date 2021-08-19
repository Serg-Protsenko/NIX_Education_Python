# Напишите функцию, которая будет преобразовывать цену к формату,
# отображающему до двух знаков после точки, например:
# 22.32131 -> 22.32
# 58.60125 -> 58.6
# 34.0 -> 34

# def format_price(num):
#     return "{:.2f}".format(num)

def format_price(num):
    rounding_number = round(num, 2)
    if int(rounding_number) == float(rounding_number):
        rounding_number = int(rounding_number)
    return rounding_number

print(format_price(22.32131))
print(format_price(58.60125))
print(format_price(34.0))
