
def primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
def tipo_examen_1():
    dic ={"abc" : [4,7,2,5],
          "123" : [4,7,4,11],
          "xyz" : [5,3,2,9]
          }
    contador = 0
    lista_key = list(dic.keys())
    for i in range (len(lista_key)):
        cadena = list(lista_key[i])
        p = True
        for j in range(len(cadena)):
            if cadena[j].isnumeric():
                p == True
            else:
                p = False
                break
        if p == True:
            lista = dic[lista_key[i]]
            for v in range(len(lista)):
                if primo(lista[v]):
                    contador +=1
                    if contador == 1:
                        primer_primo = lista[v]
                    elif contador == 2:
                        segundo_primo = lista[v]
    if primer_primo < segundo_primo:
        menor = primer_primo + 1
        mayor = segundo_primo
        z = False
        while menor < mayor:
            if primo(menor):
                z = True
                break
            else:
                menor +=1
        if z == False:
            print("son consecutivos ")
        elif z == True:
            print("no son consecutivos")
    else:
        if primer_primo > segundo_primo:
            menor = segundo_primo + 1
            mayor = primer_primo
            z = False
            while menor < mayor:
                if primo(menor):
                    z = True
                    break
                else:
                    menor +=1
            if z == False:
                print("son consecutivos ")
            elif z == True:
                print("no son consecutivos")


def tipo_examen_2():
    #llenar con -5 las posiciones comprendidas entre 0,3 y 2,1 de la matriz
    matriz =[
        [7,2,9,4],
        [5,3,2,1],
        [7,9,6,4],
    ]
    i,j,x,y = 0, 3, 2, 1
    b = 0
    while i < len(matriz) and b == 0:
        while j < len(matriz[0]) and b == 0:
            if i == x and j == y:
                matriz[i][j] = -5
                b=1
            else:
                matriz[i][j] = -5
            j += 1
        i += 1
        j = 0
    print ("matriz resultante : ")
    for i in matriz:
        print(i)

def tipo_examen_3():
    #se tienen 3 cadenas determinar los digitos comunes de estas cadenas y las letras comunes
    set_1 = int(input("ingrese su cadena N° 1"))
    set_2 = int(input("ingrese su cadena N° 2"))
    set_3 = int(input("ingrese su cadena N° 3"))
    list_set_1 = list(set_1)
    list_set_2 = list(set_2)
    list_set_3 = list(set_3)
    list_digit = []
    list_alpha = []
    for i in range(len(list_set_1)):
        aux = list_set_1[i]
        if aux in list_set_2 and list_set_3:
            if aux.isdigit():
                list_digit.append(aux)
            elif aux.isalpha():
                list_alpha.append(aux)
    print(f"los digitos comunes son : {list_digit}, y las letras son : {list_alpha}")


