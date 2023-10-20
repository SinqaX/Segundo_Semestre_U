
import random
import math

def leerVectorR():
    cd = int(input('Cantidad de datos lista -> '))
    lista = [random.randint(1, 10) for _ in range(cd)]
    return lista

def leerMatriz():
    nf = int(input('Cantidad de filas matriz -> '))
    nc = int(input('Cantidad de columnas matriz -> '))
    matriz = [[random.randint(1, 10) for _ in range(nc)] for _ in range(nf)]
    return matriz

def primo(valor):
    if valor <= 1:
        return False
    for i in range(2, int(math.sqrt(valor)) + 1):
        if valor % i == 0:
            return False
    return True

def factorial(dato):
    factorial = dato
    multiplo = dato - 1
    while multiplo > 0:
        factorial = factorial * multiplo
        multiplo -= 1
    return factorial

def fibonacci(valor):
    a, b, t = 0, 1, 0
    while t < valor:
        t = a + b
        a = b
        b = t
    if t == valor:
        return True
    else:
        return False



        








