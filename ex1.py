# -*- coding: utf-8 -*-
from collections import defaultdict

def alg(n):
    # количество сумм цифр для n=1 
    sums1 = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # построение столбцов таблицы до требуемого n
    for i in range(1, n):
        sums2 = []
        # расчёт значений соответствующих ячеек таблицы
        for j in range(len(sums1) + 10):
            sums2.append(sum(sums1[max(0, j - 10): j]))
        sums1 = sums2
    # расчёт количества счастливых билетов
    return sum(x * x for x in sums1)