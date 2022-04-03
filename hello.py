
"""
Declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
"""
list1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(f"Lista initiala: {list1}")

"""
Afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă).
"""
list2 = list1.copy()
list2.sort(reverse=False)
print(f"Lista ordonata crescator: {list2}")

"""
Afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă).
"""
list3 = list1.copy()
list3.sort(reverse=True)
print(f"Lista ordonata descrescator: {list3}")

"""
Afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă).
"""

even_numbers = list2[1::2]
print(f"Numerele pare sunt: {even_numbers}")

"""
Afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă).
"""

odd_numbers = list2[::2]
print(f"Numerele impare sunt: {odd_numbers}")

"""
Afișarea elementelor multipli ai lui 3.
"""

for number in list2:
    if number % 3 == 0:
        print(f"{number} este multiplu de 3")