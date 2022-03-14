print('Задача 8. Пирамидка')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.

# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

#
###
#####
#######

height = int(input('Введите высоту пирамиды: '))
max_char = height * 2 - 1
count_char = 0

for row in range(1, height + 1):
    count_char = row * 2 - 1
    #for col in range(max_char):
    print(' ' * (max_char - count_char), end='')
    print('#' * row, end='')
    print(' ' * (max_char - count_char), end='\n')
