# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
from math import gcd
import fractions

n1, d1 = map(int, input(
    'Введите дробь через "/": ').split('/'))
n2, d2 = map(int, input(
    'Введите дробь через "/": ').split('/'))


def sum(n1, d1, n2, d2):
    if d1 == d2:
        print('{}/{}'.format(n1 + n2, d1) if n1 +
              n2 != d1 else int(d1 / (n1 + n2)))
    else:
        cd = int(d1*d2/gcd(d1, d2))
        rn = int(n1*(cd/d1)+n2*(cd/d2))
        g = gcd(cd, rn)
        n3 = int(rn / g)
        d3 = int(cd / g)
        print('Сумма = {}/{}'.format(n3, d3)
              if n3 != d3 else 'Сумма = {}'.format(n3))

    print('Проверка: ', fractions.Fraction(
        n1, d1) + fractions.Fraction(n2, d2))


def mult(n1, d1, n2, d2):
    rn = n1 * n2
    cd = d1 * d2
    n3 = int(rn / gcd(rn, cd))
    d3 = int(cd / gcd(rn, cd))
    print('Произведение = {}/{}'.format(n3, d3) if n3 !=
          d3 else 'Произведение = {}'.format(n3))
    print('Проверка: ', fractions.Fraction(
        n1, d1) * fractions.Fraction(n2, d2))


sum(n1, d1, n2, d2)
mult(n1, d1, n2, d2)
