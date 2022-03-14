print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

max_number = 0
max_sum = 0
sum_number = 0

while True:
    text_number = input('Введите число: ')
    if text_number == '0':
        break

    for char in text_number:
        sum_number += int(char)

    if sum_number > max_sum:
        max_number = int(text_number)
        max_sum = sum_number

    sum_number = 0
    print(f'Наибольшее по сумме цифр введенное число {max_number}, сумма его цифр {max_sum}')
