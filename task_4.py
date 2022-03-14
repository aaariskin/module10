print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)

# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^

side = 10

for row in range(side):
    for col in range(side):
        if col == row or col == (side - 1) - row:
            print('^', end='')
        else:
            print(' ', end='')
    print()
