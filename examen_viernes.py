lista = [7,7,7,4,8,4,5,6,4,4,4,4]
matriz = [
    [4,4,4,4],
    [20,7,4,3],
    [4,4,4,4],
    [4,4,1,4]
]

def primo(dato):
    if dato < 2:
        return False
    for i in range(2, dato):
        if dato % i == 0:
            return False
    return True

def fibonacci(dato):
    a, b, t = 0, 1, 0
    while t < dato:
        t = a + b
        a = b
        b = t
    if t == dato:
        return True
    else:
        return False
def punto_1():
    lista = [7,7,7,4,8,4,5,6,4,4,4,4]
    matriz = [
        [4,4,4,4],
        [20,7,4,3],
        [4,4,4,4],
        [4,4,1,4]
    ]
    z = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if primo(matriz[i][j]):
                if z == 0:
                    prim_may = matriz[i][j]
                    primo_men = matriz[i][j]
                    prim_may_i = i
                    prim_men_i = i
                    prim_may_j = j
                    prim_men_j = j
                    z = 1
                else:
                    if matriz[i][j] > prim_may:
                        prim_may = matriz[i][j]
                        prim_may_i = i
                        prim_may_j = j
                    elif matriz[i][j] < primo_men:
                        primo_men = matriz[i][j]
                        prim_men_i = i
                        prim_men_j = j

    i, j, x, y = prim_may_i, prim_may_j, prim_men_i, prim_men_j
    b = 0
    contador = 0
    primer_prim = 0
    segundo_prim = 0

    while i < len(matriz) and b == 0:
        while j < len(matriz[0]) and b == 0:
            if i == j and x == y:
                b = 1
            else:
                if primo(matriz[i][j]):
                    contador += 1
                    if contador == 1:
                        primer_prim = matriz[i][j]
                    elif contador == 2:
                        segundo_prim = matriz[i][j]
            j += 1
        j = 0
        i += 1

    contador = 0
    segundo_fibo = 0
    segundo_fibo_i = 0

    while segundo_prim < len(lista):
        if fibonacci(lista[segundo_prim]):
            contador += 1
            if contador == 2:
                segundo_fibo = lista[segundo_prim]
                segundo_fibo_i = segundo_prim
        segundo_prim += 1

    print(f"El segundo Fibonacci entre el rango dado por el primer y segundo primo en la matriz dada por el primo mayor y menor es: {segundo_fibo} y su posición en el vector es: {segundo_fibo_i}")


#SEGUNDO PUNTO

dic = {
    3 : [4,9,19],
    4 : [13,4,9],
    8 : [4,5,10],
    13 : [2,4,4,8]
}
def punto_2():
    def primo_mayor_en_diccionario(diccionario):
        primo_mayor = None  # Inicializamos a None para capturar el primer número primo
        for lista in diccionario.values():  # Iteramos a través de todas las listas en el diccionario
            for numero in lista:
                if primo(numero):
                    if primo_mayor is None or numero > primo_mayor:
                        primo_mayor = numero
        return primo_mayor
    def encontrar_clave_por_valor(diccionario, valor_buscado):
        for clave, lista in diccionario.items():
            if valor_buscado in lista:
                return clave
        return None
    def fibo_men_en_diccionario(diccionario):
        fibo_menor = None
        for lista in diccionario.values():
            for numero in lista:
                if fibonacci(numero):
                    if fibo_menor is None or numero < fibo_menor:
                        fibo_menor = numero
        return fibo_menor
    lista_par = []
    primo_may = primo_mayor_en_diccionario(dic)
    fibo_men = fibo_men_en_diccionario(dic)
    key_prim = encontrar_clave_por_valor(dic, primo_may)
    key_fibo = encontrar_clave_por_valor(dic, fibo_men)
    if key_fibo < key_prim:
        while key_fibo < key_prim:
            if key_fibo % 2 == 0:
                lista_par.append(key_fibo)
            key_fibo +=1
    else:
        while key_prim < key_fibo:
            if key_prim % 2 == 0:
                lista_par.append(key_prim)
            key_prim += 1

    print(lista_par)

def punto_3():
    set_1 = set()
    set_2 = set()

    for clave, valores in dic.items():
        if primo(clave):
            for valor in valores:
                if valor % 2 == 0:  # Verifica si el valor es par
                    set_1.add(valor)
        if fibonacci(clave):
            for valor in valores:
                if valor % 2 == 0:
                    set_2.add(valor)
    cadena_1 = str(set_1 & set_2)
    cadena_2 = str(set_1 ^ set_2)

    print(f"primoos : {set_1}")
    print(f"fibos : {set_2}")
    print(f"cadena 1 : {cadena_1}")
    print(f"cadena 2 : {cadena_2}")

punto_3()  