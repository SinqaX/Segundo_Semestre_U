cad="esto es una cadena"
# print(len(cad))
# for i in range(len(cad)):
#     print(cad[i])
# cad1="esto"
# cad2="es"
# cad3="una cadena"
cad4="esto es una cadena"
# print(cad4[5:15:3])#inicio:fin:step
# cad4[:]
# #len()
# print(str(True))#convierte el parametro en cadena
# cad=""
# l1=["a","b","c"]
# for i in range(len(l1)):
#     cad+=l1[i]#concatena
# #print(cad)

# #buscar una subcadena
# #utiliza in 
# if "esto" in cad4:
#     print("true")

#funcion find
# print(cad4.find("esto"))#entrega el indice donde esta la cadena solamente del primero

#funcion index
# print(cad4.index("es"))#entrega el indice donde esta la cadena solamente del primero
# print("537".isnumeric())#=true
# print("25.5".isnumeric())#=False
# print("cad".isalpha())#=true ya que tiene letras
# print("9".isdigit())
# print(cad.upper())#mayusculas
# print(cad.lower())#minuscula

#relacion entre cadenas y listas
list()#convierte a lista cualquier elemento iterable
cd="Hola Mundo"
# l=list(cd)#cuando se convierte se puede modificar
# l.sort()#ordena
# print(l)
# z="".join(l)#concatena una lista a string join pertenece a las listas no es una funcion de cadena
# print(z)

# #cambiar una subcadena

# cd.replace("mundo", "hola")
# cd.replace("o", "a")

#funcion split y funcion sprit

#print(cad4.split())#coje las palabras y las vuelve lista y si encuentra un espacio separa la palabra 
# #dentro del parentesis uno puede colocar algo para que el bloque se separe como una ,
# #el sprit elimina caracteres especiales como \n(nueva linea ) \t(retorno de carril)
# print(cad4.strip())
# cadena = "   Esto es una cadena con espacios en blanco al principio y al final.   "

# # Utiliza strip() para eliminar los espacios en blanco al principio y al final.
# cadena_limpia = cadena.strip()
# print(cadena)
# print(cadena_limpia)

#funcion count cuenta un valor que le ingreses



l = [(7,5),(8,3),(9,7)]
lo = dict(sorted(l, key = lambda t : t[0]))
print(lo)











