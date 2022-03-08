

from functools import reduce


def mi_filter():
    mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # pares = []
    # for i in mi_lista:
    #     if i % 2 == 0:
    #         pares.append(i)

    # pares = [i for i in mi_lista if i % 2 == 0]

    pares = list(filter(lambda i: i % 2 == 0, mi_lista))

    print(pares)

def mi_map():
    lista = [1, 2, 3, 4, 5]

    # cuadrados = []

    # for i in lista:
    #     cuadrados.append(i ** 2)

    # cuadrados = [i ** 2 for i in lista]

    cuadrados = list(map(lambda i: i ** 2, lista))

    print(cuadrados)

def mi_reduce():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # suma = 0
    # for i in lista:
    #     suma += i

    # print(suma)

    resultado = reduce(lambda a, b: a * b, lista)
    print(resultado)

if __name__ == '__main__':
    mi_reduce()