# 1.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, 
# determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada, 
# es un numero Fibonacci, si no lo es determinar si es primo y su factorial.
import random 

def leerMatriz():
    nf = int(input('Cantidad de filas matriz -> '))
    nc = int(input('Cantidad de columnas matriz -> '))
    matriz = [[random.randint(1, 10) for _ in range(nc)] for _ in range(nf)]
    return matriz

def leerVectorR():
    cd = int(input('Cantidad de datos lista -> '))
    lista = [random.randint(1, 10) for _ in range(cd)]
    return lista

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

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def factorial(dato):
    factorial=dato
    multiplo=dato-1
    while multiplo>0:
        factorial=factorial*multiplo
        multiplo-=1
    return factorial




def punto_1_matrices():
    print("""1.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, 
          determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada, 
          es un numero Fibonacci, si no lo es determinar si es primo y su factorial."""
          )
    perimetro=0
    matriz=leerMatriz()
    z=0
    x=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j==0:
                a=matriz[i][j]
            elif j==1:
                b=matriz[i][j]
            elif j==2:
                c=matriz[i][j]    
        
        if a==b==c:
            z+=1
            if z==2 or z==4:
                perimetro+=a+b+c
                
        if a!=b!=c!=a:
            x+=1
            if x==2:
                perimetro+=a+b+c
                
    valor = perimetro        
    print("la matriz ingresada es ")
    for i in matriz:
        print(i)
    if fibonacci(valor):
        print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero fibonacci : {perimetro}")
    elif primo(valor):
            print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero primo : {perimetro}, y su factorial es : {factorial(perimetro)}")
    else:
        print(f"la suma de los perimetros del segundo y cuarto equilatero y el segundo escaleno : {perimetro}, no es ni fibonacci ni primo")


def punto_3_listas():
    print("""3.	Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.\n""")
    lista_1=leerVectorR()
    lista_2=leerVectorR()
    lista_primos=[]
    print(f"lista ingresada N° 1 : {lista_1}")
    print(f"lista ingresada N° 2 : {lista_2}")
    for i in range(len(lista_1)):
        if primo(lista_1[i]):
            if lista_1[i] not in lista_primos and lista_1[i]  in lista_2:
                lista_primos.append(lista_1[i])

    print(f"la lista con los primos  comunes sin repetidos es : {lista_primos}")
                

def punto_5_matrices():
    print("""5.	Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, 
           determinar si la suma de los perímetros del segundo, cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada,
           es un numero Fibonacci, si no lo es determinar si es primo y su factorial.
        """)
    perimetro=0
    matriz=leerMatriz()
    z=0
    x=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j==0:
                a=matriz[i][j]
            elif j==1:
                b=matriz[i][j]
            elif j==2:
                c=matriz[i][j]    
        
        if a==b==c:
            z+=1
            if z==2 or z==4:
                perimetro+=a+b+c
                
        if a!=b!=c!=a:
            x+=1
            if x==2:
                perimetro+=a+b+c
                
    valor = perimetro        
    print("la matriz ingresada es ")
    for i in matriz:
        print(i)
    if fibonacci(valor):
        print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero fibonacci : {perimetro}")
    elif primo(valor):
            print(f"la suma de perimetros del segundo y cuarto equilatero y el segundo escaleno es un numero primo : {perimetro}, y su factorial es : {factorial(perimetro)}")
    else:
        print(f"la suma de los perimetros del segundo y cuarto equilatero y el segundo escaleno : {perimetro}, no es ni fibonacci ni primo")


def punto_7_listas():
    print("""7. Se tiene un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas
                 del primo que más se repite con el primo que menos se repite.
            """)
    lista = leerVectorR()
    contador_primos = {}  # Un diccionario para contar las repeticiones de primos únicos
    
    for numero in lista:
        if primo(numero):
            if numero in contador_primos:
                contador_primos[numero] += 1
            else:
                contador_primos[numero] = 1
    
    primos = list(contador_primos.keys())  # Lista de primos únicos
    primos.sort(key=lambda x: contador_primos[x])  # Ordena la lista de primos por repeticiones
    
    if len(primos) < 2:
        print("No hay suficientes primos en la lista.")
        return
    
    primo_menos_repetido = primos[0]
    primo_mas_repetido = primos[-1]
    
    resultado = primo_menos_repetido * primo_mas_repetido
    
    print(f"""
          El vector ingresado para el ejercicio fue : {lista}, 
          El primo que menos se repitió de la lista fue : {primo_menos_repetido} con {contador_primos[primo_menos_repetido]} repeticiones,
          El más repetido fue : {primo_mas_repetido} con {contador_primos[primo_mas_repetido]} repeticiones,
          La multiplicación de estos dos primos fue : {resultado}
            """)

def punto_9_listas():
    print("""9. Se tiene un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas
                 del primo que más se repite con el primo que menos se repite.
            """)
    lista = leerVectorR()
    contador_primos = {}  # Un diccionario para contar las repeticiones de primos únicos
    
    for numero in lista:
        if primo(numero):
            if numero in contador_primos:
                contador_primos[numero] += 1
            else:
                contador_primos[numero] = 1
    
    primos = list(contador_primos.keys())  # Lista de primos únicos
    primos.sort(key=lambda x: contador_primos[x])  # Ordena la lista de primos por repeticiones
    
    if len(primos) < 2:
        print("No hay suficientes primos en la lista.")
        return
    
    primo_menos_repetido = primos[0]
    primo_mas_repetido = primos[-1]
    
    resultado = primo_menos_repetido * primo_mas_repetido
    
    print(f"""
          El vector ingresado para el ejercicio fue : {lista}, 
          El primo que menos se repitió de la lista fue : {primo_menos_repetido} con {contador_primos[primo_menos_repetido]} repeticiones,
          El más repetido fue : {primo_mas_repetido} con {contador_primos[primo_mas_repetido]} repeticiones,
          La multiplicación de estos dos primos fue : {resultado}
            """)



def punto_11_matrices():
    print("11.	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos ")
    matriz=[
        [4,5,3,4],
        [4,4,4,4],
        [3,3,4,4]
    ]
    
    print("matriz a trabajar : ")
    for i in matriz:
        print(i)
    
    primos = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz[0])) if primo(matriz[i][j])]
    
    if len(primos) < 4:
        print("No se encontraron los primos 2 y 4 en la matriz.")
    else:
        consecutivos = primos[3] - primos[1] == 2
        for i in range(1, len(primos) - 2):
            if primos[i+2] - primos[i] == 2:
                consecutivos = False
                break

        if consecutivos:
            print(f"El primo 2 ({primos[1]}) y el primo 4 ({primos[3]}) son consecutivos.")
        else:
            print(f"Entre el primo 2 ({primos[1]}) y el primo 4 ({primos[3]}) hay números primos, por lo tanto, no son consecutivos.")

    
    

def punto_13_listas_y_matrices():
    print("""
    13. Se tiene un conjunto y una matriz con datos numéricos,
    hallar el primo mayor del conjunto y su factorial y llenar este valor en las posiciones comprendidas
    entre el par menor y el Fibonacci mayor de la matriz
    """)
    lista = [2, 3, 6, 8, 10, 7]
    matriz = [
        [2, 3, 6],
        [4, 10, 8],
        [10, 7, 5]
    ]

    z = 0
    f = 0
    p = 0

    for i in range(len(lista)):
        if primo(lista[i]):
            if z == 0:
                primo_mayor = lista[i]
                z = 1
            elif lista[i] > primo_mayor:
                primo_mayor = lista[i]

    factor = factorial(primo_mayor)

    print(f"la lista ingresada es : {lista}")

    print("la matriz ingresada es : \n")
    for i in matriz:
        print(i)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if fibonacci(matriz[i][j]):
                if f == 0:
                    fibonacci_mayor = matriz[i][j]
                    fibonacci_mayor_i = i
                    fibonacci_mayor_j = j
                    f = 1
                elif matriz[i][j] > fibonacci_mayor:
                    fibonacci_mayor = matriz[i][j]
                    fibonacci_mayor_i = i
                    fibonacci_mayor_j = j
            if matriz[i][j] % 2 == 0:
                if p == 0:
                    par_menor = matriz[i][j]
                    par_menor_i = i
                    par_menor_j = j
                    p = 1
                elif matriz[i][j] < par_menor:
                    par_menor = matriz[i][j]
                    par_menor_i = i
                    par_menor_j = j

    if par_menor_i < fibonacci_mayor_i:
        for i in range(par_menor_i, fibonacci_mayor_i + 1):
            for j in range(par_menor_j, fibonacci_mayor_j + 1):
                matriz[i][j] = factor
    elif par_menor_i > fibonacci_mayor_i:
        for i in range(fibonacci_mayor_i, par_menor_i + 1):
            for j in range(fibonacci_mayor_j, par_menor_j + 1):
                matriz[i][j] = factor


    print(f"el primo mayor del conjunto es : {primo_mayor} y su factorial es : {factor}")
    print(f"el par menor de la matriz es : {par_menor} con posición i: {par_menor_i + 1} y j: {par_menor_j + 1}")
    print(f"el Fibonacci mayor de la matriz es : {fibonacci_mayor} con posición i: {fibonacci_mayor_i + 1} y j: {fibonacci_mayor_j + 1}")
    print(" y la matriz resultante del ejercicio queda :")
    for i in matriz:
        print(i)


def contar_primos_en_matrices(matriz_1, matriz_2):
    diccionario = {}
    
    for fila in matriz_1:
        for numero in fila:
            if primo(numero):
                if numero in diccionario:
                    diccionario[numero] += 1
                else:
                    diccionario[numero] = 1
    
    for fila in matriz_2:
        for numero in fila:
            if primo(numero):
                if numero in diccionario:
                    diccionario[numero] += 1
                else:
                    diccionario[numero] = 1

    return diccionario

def punto_15_diccionarios():
    print("15. Se tienen dos matrices con datos numéricos. Formar un diccionario con los primos como clave y las veces que aparecen como valor, ordenado por la clave.")
    matriz_1 = leerMatriz()  # Supongo que tienes una función llamada "leerMatriz" que lee la matriz.
    matriz_2 = leerMatriz()  # Debes implementar esta función también.

    print("Las matrices que se van a trabajar son:")
    print("Matriz 1\n")
    for fila in matriz_1:
        print(fila)
    print("\nMatriz 2\n")
    for fila in matriz_2:
        print(fila)

    diccionario_final = contar_primos_en_matrices(matriz_1, matriz_2)

    # Ordenar el diccionario por las claves.
    diccionario_ordenado = dict(sorted(diccionario_final.items()))

    print(f"Los primos de las matrices y las veces que se repiten son: {diccionario_ordenado}")

def contar_caracteres(cadena):
    diccionario_digito = {}
    diccionario_caracter = {}

    for caracter in cadena:
        if caracter.isdigit():
            if caracter in diccionario_digito:
                diccionario_digito[caracter] += 1
            else:
                diccionario_digito[caracter] = 1
        elif caracter.isalpha():
            if caracter in diccionario_caracter:
                diccionario_caracter[caracter] += 1
            else:
                diccionario_caracter[caracter] = 1

    return diccionario_digito, diccionario_caracter

def punto_17_diccionarios():
    print("""
    17.	Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
    Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
    Diccionario 2 con clave carácter y valor las veces que se repite, ordena el do ascendentemente por clave 
    """)
    cadena_1 =input("ingrese su cadena alfanumerica N° 1")
    cadena_2 =input("ingrese su cadena alfanumerica N° 2")
    cadena_3 =input("ingrese su cadena alfanumerica N° 3")
    cadena_final = cadena_1 + cadena_2 + cadena_3
    dic_digito, dic_caracter = contar_caracteres(cadena_final)
    dic_digito_final = dict(sorted(dic_digito.items(), key = lambda t : t[0]))
    dic_caracter_final = dict(sorted(dic_caracter.items(), key = lambda t : t[0]))
    print(f"diccionario con digitos : {dic_digito_final}, diccionario con caracteres : {dic_caracter_final}")




def punto_19_diccionarios():
    print("""
    19.	Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
    el par mayor y las veces que se repite
    el primo menor y las veces que se repite
    el Fibonacci menor y las veces que se repite
    Con estos datos hallar:
    El factorial de la suma del par y del primo
    La multiplicación con sumas de los contadores del primo y del Fibonacci.

    """)
    lista = [5,5,4,4,9,9,9,6,6,3,1,1,21,21,13,13,13,13,21]
    matriz = [
        [4,5,9,6,3],
        [21,13,6,9,12],
        [5,4,3,1,6]
    ]
    l_par = []
    l_primo = []
    l_fibonacci = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            l_par.append(lista[i])
        elif primo(lista[i]):
            l_primo.append(lista[i])
        elif fibonacci(lista[i]):
            l_fibonacci.append(lista[i])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                l_par.append(matriz[i][j])
            elif primo(matriz[i][j]):
                l_primo.append(matriz[i][j])
            elif fibonacci(matriz[i][j]):
                l_fibonacci.append(matriz[i][j])
    par_mayor = max(l_par)
    rep_par = lista.count(par_mayor) + matriz.count(par_mayor)
    primo_menor = min(l_primo)
    rep_primo = lista.count(primo_menor) + matriz.count(primo_menor)
    fibonacci_menor = min(l_fibonacci)
    rep_fibo = lista.count(fibonacci_menor) + matriz.count(fibonacci_menor)

    sum_fib_pri = primo_menor + par_mayor
    fac_sum_fib_pri = factorial(sum_fib_pri)
    
    men = 0
    r = 0
    while men < rep_fibo:
        r += rep_primo
        men += 1
    print(f"""
    el par mayor : {par_mayor} las veces que se repite : {rep_par}
    el primo menor : {primo_menor} las veces que se repite : {rep_primo}
    el Fibonacci menor : {fibonacci_menor} las veces que se repite : {rep_fibo}
    El factorial de la suma del par y del primo : {fac_sum_fib_pri}
    La multiplicación con sumas de los contadores del primo y del Fibonacci : {r}
    """)
            
punto_19_diccionarios()



