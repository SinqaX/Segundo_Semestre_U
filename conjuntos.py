#conjuntos = set
#con set elimina elementos repetidos para una lista
# interseccion = elementos comunes de los conjuntos 
# diferencia simetricra = es la union eliminando la interseccion 

#DIFERENCIA
# for i in range(len(lista_1)):
#         aux = lista_1[i]
#         if aux not in lista_2:
#             diferencia.add(aux)

# A - B
#A.difference(B)

#INTERSECCION
#     for i in range(len(lista_1)):
#         aux = lista_1[i]
#         if aux in lista_2:
#             interseccion.add(aux)

# A & B
#A.intersection(B)

#UNION
#     for i in range(len(lista_1)):
#         union.add(lista_1[i])
#     for j in range(len(lista_2)):
#         union.add(lista_2[j])
        
# A | B
# A.union(B)

#DIFERNECIA SIMETRICA
#     lista_union = list(union)
#     for i in range(len(lista_union)):
#         if lista_union[i] in union and lista_union[i] not in interseccion:
#             diferencia_simetrica.add(lista_union[i])

# A ^ B 
# A.symmetric_difference(B)


