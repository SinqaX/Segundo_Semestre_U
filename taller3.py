import os
def menu_vectores():
    while True:
        os.system('cls')
        print('Menú vectores')
        print('---------------------------------')
        print('   1. Ejercicios con un solo vector')
        print('   2. Ejercicios con varios vectores')
        print('')
        print('  3. Regresar')
        print('--------------------------------')
        # ingresar una opcion
        opcion =int(input('Elija una opción (1-3): '))
        match opcion:
            case 1:
                menu_vectores1()
                os.system('pause')
            case 2:
                print('menu con varios vectores ')
                os.system('pause')
                        
            case 3:
                print('Regresa al menu anterior ')
                break
            case other: 
                print('Ha digitado una opción invalida ')
                os.system("pause")
                
def menu_vectores1():
    sw=False    
    while True:
        os.system('cls')
        print('Menú vectores')
        print('---------------------------------')
        print('   1. Leer vector')
        print('   2. Mostrar vector')
        print('   3. Mayor, menor, promedio del  vector')
        print('   4. primos del vector')
        print('   5. Promedio primos vector')
        print('')
        print('  6. Regresar ')
        print('--------------------------------')
        # ingresar una opcion
        opcion =int(input('Elija una opción (1-3): '))
        match opcion:
            case 1:
                vec=leerVector()
                os.system('pause')
                sw=True
            case 2:
                if sw==True:
                    mostrarVector(vec)
                    os.system('pause')
                else:
                    print('No hay vector. Realizar opcion 1')
                    os.system('pause')
            case 3:
                print('Se va a ordenar un vector ')
                os.system('pause')
            case 4:
                print('mayor menor y promedio de un vector de un vector ')
                os.system('pause')
            case 5:
                print('Promedio de los primos del vector ')
                os.system('pause')
                        
            case 6:
                print('Regresa al menú anterior ')
                break
            case other: 
                print('Ha digitado una opción invalida ')
                os.system("pause")

def leerVector():
    print('Lectura del vector')
    cd=int(input('cantidad de datos ->'))
    vec=[]
    for i in range(cd):
        vec.append(int(input(f'Digitar dato ({i}) ->')))
    return vec

def mostrarVector(vec):
    print('Se va mostrar el vector ')
    for  i in range(len(vec)):
        print(f'Dato [{i}] ->   {vec[i]} ')

def menuPrincipal():
    while True:
        os.system('cls')
        print('Menú de operaciones con vector')
        print('---------------------------------')
        print('   1. Ejercicios vectores')
        print('   2. Ejercicios matrices')
        print('   3. Ejercicios vectores matrices ')
        print('   4. Ejercicios cadenas ')
        print('   ')
        print('   5. Salir')
        print('')
        print('--------------------------------')
        # ingresar una opcion
        opcion =int(input('Elija una opción (1-5): '))
        match opcion:
            case 1:
                menu_vectores()
                os.system('pause')
            case 2:
                print('Llama menú matrices ')
                os.system('pause')
            case 3:
                print('llama menu vectores matrices ')
                os.system('pause')
            case 4:
                print('llama menu cadenas ')
                os.system('pause')
                        
            case 5:
                print('Gracias por su visita ')
                break
            case other: 
                print('Ha digitado una opción invalida ')
                os.system("pause")

#programa principal
menuPrincipal()