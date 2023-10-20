#Funcion que recibe un parámetro correspondiente a una lista, la modifica y #los valores se van a reflejar en el programa que lo llama
import random
import math
def leerVectorR():
    cd = int(input('Cantidad de datos lista -> '))
    lista = [random.randint(1, 10) for _ in range(cd)]
    return lista


#funcion que lee una matriz

def leerMatriz():
    nf = int(input('Cantidad de filas matriz -> '))
    nc = int(input('Cantidad de columnas matriz -> '))
    matriz = [[random.randint(1, 10) for _ in range(nc)] for _ in range(nf)]
    return matriz


#determinar si un valor dado es fibonacci

def fibonacci(valor):
    a=0
    b=1
    t=0
    while t<valor :
        t=a+b
        a=b
        b=t
    if t==valor:
        return True
    else:
        return False
    
#determinar si un valor es primo 

def es_primo(valor):
    if valor <= 1:
        return False
    for i in range(2, int(math.sqrt(valor)) + 1):
        if valor % i == 0:
            return False
    return True  

#determinar si un valor es impar

def es_impar(valor):
    if valor % 2 == 0:
        return False
    else:
        return True

#ordenamiento de un vector ascendentenmente

def orden_ascendente(lista):
    for i in range(len(lista)):
        me=i
        for j in range(i+1, len(lista)):
            if lista[j]<lista[me]:
                me=j
        lista[i],lista[me]=lista[me],lista[i]

#ordenamiento de un vector descendentemente

def orden_descendente(lista):
    for i in range(len(lista)):
        me=i
        for j in range(i+1, len(lista)):
            if lista[j]>lista[me]:
                me=j
        lista[i],lista[me]=lista[me],lista[i]

        

