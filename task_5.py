print('Задача 5. Простые числа')

#Напишите программу,
#которая считает количество простых чисел в заданной последовательности
#и выводит ответ на экран.

start = int(input('Введите начало последовательности: '))
end = int(input('Введите конец последовательности: '))
flag_no_simple = ''
count_simple_number = 0

for number in range(start, end + 1):
    for devider in range(1, number + 1):
        if number == 1 or (number % devider == 0 and devider != 1
                           and devider != number):
            flag_no_simple = 'x'
    if flag_no_simple != 'x':
        count_simple_number += 1
    flag_no_simple = ''

print(
    f'Количество простых чисел в последовательности от {start} до {end} равно {count_simple_number}'
)
