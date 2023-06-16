"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
import random

min_border = 0
max_border = 1001
guess_number = random.randint(min_border, max_border)
try_count = 1
while True:
    input_number = int(input('Введите число: '))
    if try_count >= 10:
        print("Ты израсходовал все свои попытки!")
        break
    else:
        if guess_number == input_number:
            print('Ура!!! ты угадал!')
            break
        elif guess_number < input_number:
            print('Моё число меньше. у вас осталось ' +
                  str(10 - try_count) + ' попыток.')
        elif guess_number > input_number:
            print('Моё число больше. у вас осталось ' +
                  str(10 - try_count) + ' попыток.')
        try_count += 1

print('я загадал ' + str(guess_number))
