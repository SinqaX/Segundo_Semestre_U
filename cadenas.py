### ejercicios cadenas###

#1  se tiene una cadena contar las veces que se repite un caracter 
#2  se tiene una cadena ordenarla en forma ascenedete y en forma descendente
#3  convertir la cadena a mayusculas y minusculas 
#4  de una cadena dada donde hay digitos y caracteres alfabetico formar dos cadenas , cadena1 con los digitos sin repetidos cadena2 con los alfabeticos sin repetidos
#5  se tienen dos cadenas formar dos cadenas cadena 1 con los digitos no comunes de las dos cadenas y cadena 2 con las letras comunes de las dos cadenas sin repetir
#6  determinar cuantas palabras hay en un parrafo
#7  remplazar un caracter de una cadena por otro caracter dado
#8  se tiene una cadena sacar cual es el caracter que mas se repite

def punto_1_cadenas():
    print("1  se tiene una cadena contar las veces que se repite un caracter ")
    cadena=input("ingresar su frase")
    contar=input("ingrese el caracter a contar")
    print(f"la letra k se repite en la cadena : {cadena.count(contar)} veces")

def punto_2_cadenas():
    print("2. Se tiene una cadena, ordenarla en forma ascendente y en forma descendente")
    cadena = input("Ingrese su frase: ")
    lista_cadena = list(cadena)

    lista_cadena_ascendente = sorted(lista_cadena)
    lista_cadena_descendente = sorted(lista_cadena, reverse=True)

    cadena_ascendente = ''.join(lista_cadena_ascendente)
    cadena_descendente = ''.join(lista_cadena_descendente)

    print("Cadena ordenada en forma ascendente:", cadena_ascendente)
    print("Cadena ordenada en forma descendente:", cadena_descendente)

def punto_3_cadenas():
    print("3  convertir la cadena a mayusculas y minusculas ")
    cadena = input("Ingrese su frase: ")
    print(f"su cadena es mayusculas es :  {cadena.upper()}")
    print(f"su cadena en minusculas es : {cadena.lower()}")
    
def punto_4_cadenas():
    print("""
        de una cadena dada donde hay digitos y caracteres alfabetico formar dos cadenas , 
          -cadena1 con los digitos sin repetidos 
          -cadena2 con los alfabeticos sin repetidos
    """)
    string = (input("ingresar su cadena -> "))
    set_digit = set()
    set_alpha = set()
    list_string = list(string)
    for i in range(len(list_string)):
        if list_string[i].isdigit():
            set_digit.add(list_string[i])
        elif list_string[i].isalpha():
            set_alpha.add(list_string[i])
    str_digit = str(set_digit)
    str_alpha = str(set_alpha)
    print(f"cadena con digitos :{str_digit}, cadena con alphas : {str_alpha}")

def punto_5_cadenas():
    print("""
    #5  se tienen dos cadenas formar dos cadenas 
          -cadena 1 con los digitos no comunes de las dos cadenas 
          -cadena 2 con las letras comunes de las dos cadenas sin repetir
    """)

    

