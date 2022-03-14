print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

user_number = int(input('Введите число: '))
sum_fact = 0
factorial = 1

for number in range(1, user_number + 1):
    for fact_number in range(1, number + 1):
        factorial *= fact_number
    sum_fact += factorial
    factorial = 1

print(f'Сумма факториалов числа {user_number} равна {sum_fact}')