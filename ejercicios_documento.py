import random     
import math    
def valor_entero():
    while True : 
        try :
            a = int(input("digite valor"))
        except ValueError:
            print("error : el valor digitado no es entero, vuelva a ingresar el valor")
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

def leerMatriz():
    nf = int(input('Cantidad de filas matriz -> '))
    nc = int(input('Cantidad de columnas matriz -> '))
    matriz = [[random.randint(1, 20) for _ in range(nc)] for _ in range(nf)]
    return matriz

#se tienen dos ematrices formar dos conjuntos con los numeros primos de cada matriz  y con estos dos conjuntos hallar 
# la interseccion
# la union 
# la difernecia 
# y la diferencia simetrica

# c1 = {7, 5, 3, 2, 11}
# c2 = {7, 2, 13, 19}

# c1 - c2 = { 5, 3, 11}  diferencia
# c1 & c2 = {7, 2} interseccion 
# c1 | c2 = {7, 5, 3, 2, 11, 13, 19}  union
# c1 * c2 = {5, 3, 11, 13, 19} diferencia simetrica
def punto_1_conjuntos():
    print("""
se tienen dos ematrices formar dos conjuntos con los numeros primos de cada matriz  y con estos dos conjuntos hallar 
la interseccion
la union 
la difernecia 
y la diferencia simetrica
""")
    matriz_1 = leerMatriz()
    matriz_2 = leerMatriz()
    set_1 = {7, 5, 3, 2, 11}
    set_2 = {7, 2, 13, 19}
    diferencia = set()
    interseccion = set()
    union = set()
    diferencia_simetrica = set()
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[0])):
            if primo(matriz_1[i][j]):
                set_1.add(matriz_1[i][j])
    for i in range(len(matriz_2)):
        for j in range(len(matriz_2[0])):
            if primo(matriz_2[i][j]):
                set_2.add(matriz_2[i][j])

    lista_1 = list(set_1)
    lista_2 = list(set_2)

    for i in range(len(lista_1)):
        aux = lista_1[i]
        if aux not in lista_2:
            diferencia.add(aux)

    for i in range(len(lista_1)):
        aux = lista_1[i]
        if aux in lista_2:
            interseccion.add(aux)

    for i in range(len(lista_1)):
        union.add(lista_1[i])
    for j in range(len(lista_2)):
        union.add(lista_2[j])
        
    lista_union = list(union)
    for i in range(len(lista_union)):
        if lista_union[i] in union and lista_union[i] not in interseccion:
            diferencia_simetrica.add(lista_union[i])

    print(f"""
        conjunto 1 {set_1}
        conjunto 2 {set_2}\n
        diferencia {diferencia}
        interseccion {interseccion}
        union {union}
        diferencia simetrica {diferencia_simetrica}
        """)




#1 se tiene una matriz con datos numericos hallar el fibonacci mayor y menor y determinar cual de los dos esta antes

def punto_2_conjuntos():
    matriz = leerMatriz()
    f=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if fibonacci(matriz[i][j]):
                if f == 0:
                    fibonacci_mayor = matriz[i][j]
                    fibonacci_menor = matriz[i][j]
                    fibonacci_mayor_i = i
                    fibonacci_mayor_j = j
                    fibonacci_menor_i = i
                    fibonacci_menor_j = j
                    f = 1
                elif matriz[i][j] > fibonacci_mayor:
                    fibonacci_mayor = matriz[i][j]
                    fibonacci_mayor_i = i
                    fibonacci_mayor_j = j
                elif matriz[i][j] < fibonacci_menor:
                    fibonacci_menor = matriz[i][j]
                    fibonacci_menor_i = i
                    fibonacci_menor_j = j
    print("la matriz ha trabajar es :\n")
    for i in matriz:
        print(i)
    
    print(f"fibonacci mayor {fibonacci_mayor}")
    print(f"fibonacci menor {fibonacci_menor}")

    if fibonacci_mayor_i == fibonacci_menor_i:
        if fibonacci_mayor_j > fibonacci_menor_j:
            print("el fibonacci menor esta primero")
        else:
            print("el fibonacci mayor esta de primero")
    else:
        if fibonacci_mayor_i > fibonacci_menor_i:
            print("el fibonacci menor esta primero")
        else:
            print("el fibonacci mayor esta de primero")


#2 se tiene una matriz con datos numericos llenar las posiciones entre el primo dos y el primo 3 de esta matriz con la suma de los dos primos


#3 tipo examen : se tiene una matriz y un vector con datos numericos hallar en el vector el segun y tercer primo y el primer fibonacci
#y llenar las posiciones de la matriz comprendidas entre el primo uno y el roimo dos que tambien estan en la matriz con el primer fibonacci

#4 se tiene una matriz con datos numericos encontrar e fibonacci menor y fibonacci mayor y llenar las posiciones entre estos valores 
#con la suma de estos fibonaccis