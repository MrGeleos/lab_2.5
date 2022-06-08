#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Определить, есть ли в кортеже хотя бы одна тройка соседних чисел, в которой средний
элемент больше своих «соседей», т. е. предшествующего и последующего. В случае
положительного ответа определить номера элементов первой из таких троек.
"""

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("Заданный кортеж пуст", file=sys.stderr)
        exit(1)

    for index, i in enumerate(A):
        k1 = A[index]
        k2 = A[index + 1]
        k3 = A[index + 2]

        if k1 < k2 > k3:
            print(index, index + 1, index + 2)
            break
        