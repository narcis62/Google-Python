"""
Să se scrie un modul care contine 3 funcții recursive care primesc ca parametru un număr întreg și returnează:
1. Suma tuturor numerelor de la [0, n]
"""

suma = 0


def my_func(n):

    global suma

    if n > 0:
        suma += n
        my_func(n-1)

    return suma


my_func(11)

print(f"Suma tuturor numerelor de la [0,n], unde n=11 este: {suma}")

"""
2. Suma numerelor pare de la [0, n]
"""

suma = 0


def my_func1(n):

    global suma

    if n > 0 and n % 2 == 0:
        suma += n

        my_func1(n-1)

    elif n > 0 and n % 2 != 0:

        my_func1(n-1)

    return suma


my_func1(11)

print(f"Suma tuturor numerelor pare de la [0,n], unde n=11 este: {suma}")

"""
3. Suma numerelor impare de la [0, n]
"""

suma = 0


def my_func2(n):

    global suma

    if n > 0 and n % 2 != 0:
        suma += n

        my_func2(n-1)

    elif n > 0 and n % 2 == 0:

        my_func2(n-1)

    return suma


my_func2(11)

print(f"Suma tuturor numerelor impare de la [0,n], unde n=11 este: {suma}")