from numbers import Number

"""
Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
numere întregi sau reale.
"""


def my_function(*args):

    result = 0

    for arg in args:

        if isinstance(arg, Number):
            result += arg

    return result


print(f"Rezultatul este: {my_function(1,5,-3,'abc',[12,56,'cad'])}")


def my_function2(*args):

    if len(args) == 0:
        return 0


print(f"Functia returneaza: {my_function2()}")


def my_function1(a,b,c,**kwargs):

    return a+b


print(f"Rezultatul este: {my_function1(2,4,'abc',param_1=2)}")

"""
Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
valoarea 0.
"""


def my_function3():

    answer = input("Choose a number: ")

    if answer.isnumeric():
        print(f"{answer} este un numar.")
        return answer

    else:
        print(f"{answer} nu este un numar.")
        return 0


my_function3()

