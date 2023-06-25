# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.
import random

my_items = {'Топор': 500,
            'Одеяло': 500,
            'Котелок': 1000,
            'Еда': 2500,
            'Вода': 1000,
            'Спички': 100,
            'Палатка': 3000,
            'Мешок': 2000,
            }

tonnage = 6000
container = 0
list_items = []
while container < tonnage:
    key, val = random.choice(list(my_items.items()))
    if key not in list_items:
        if container + val > tonnage:
            break
        else:
            container += val
            list_items += (key, val)

print(list_items)
