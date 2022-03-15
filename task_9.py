print('Задача 9. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите количество уровней пирамиды: '))
number = 1
display = ''

for row in range(height):
    display = 'x'
    for col in range(1, height * 2):
        if col < (height - row) or col > (height + row) or display != 'x':
            print('\t', end='')
            display = 'x'
        else:
            print(number, end='\t')
            number += 2
            display = ''
    print()
