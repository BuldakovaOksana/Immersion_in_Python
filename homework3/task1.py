# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов

list = [1, 5, 6, 8, 6, 9, 2, 1, 3, 5, 3]
double_list = []
for i in list:
    if list.count(i) > 1:
        double_list.append(i)

print(set(double_list))
