# Программа угадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.

min_border = 0
max_border = 1001
find_number = max_border // 2
try_count = 1
temp = 1
while True:
    print('Ваше число ' + str(find_number) + '?')
    answer = input("Если я угадал нажмите 'y', если ваше число меньше нажмите '<', "
                   "если ваше число больше нажмите '>' ")
    if answer == 'y':
        print('Урааа!!! Я угадал!')
        break
    elif answer == '<':
        max_border = find_number
        find_number = (max_border - min_border) // 2 + min_border

    elif answer == '>':
        min_border = find_number
        find_number = (max_border - min_border) // 2 + min_border

    else:
        print('Вы что-то не то ввели!')
    try_count += 1
    print('Попытка № ' + str(try_count))
