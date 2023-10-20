#se teiene una lista con datos numericos formar dos listas asi: 1)con los primos sin repetir ascendentemente 2)una lista con fibonacci sin repetir descendentemente
import random

def leerVectorR(lista):
    c=int(input("cauntos datos quiere en el vector : "))
    for i in range(c):
        lista.append(random.randint(1, 10))
    return lista

def fibonacci(valor):
    a,b,t = 0,1,0
    while t<valor :
        t=a+b
        a=b
        b=t
    if t==valor:
        return True
    else:
        return False
    
def primo(valor):
        r=2
        p=False
        if valor<=1:
            return False
        else:
            while r<valor-1 and p==False:
                if valor%r==0:
                    p=True
                r+=1
            if p==False:
                return True
            else:
                return False    

def orden_ascendente(lista):
    for i in range(len(lista)):
        me=i
        for j in range(i+1, len(lista)):
            if lista[j]<lista[me]:
                me=j
        lista[i],lista[me]=lista[me],lista[i]

def orden_descendente(lista):
    for i in range(len(lista)):
        me=i
        for j in range(i+1, len(lista)):
            if lista[j]>lista[me]:
                me=j
        lista[i],lista[me]=lista[me],lista[i]

lista=[]
leerVectorR(lista)
lista_primos=[]
lista_fibonacci=[]
for i in range(len(lista)):
    if primo(lista[i]):
        if lista[i] not in lista_primos:
            lista_primos.append(lista[i])
    if fibonacci(lista[i]):
        if lista[i] not in lista_fibonacci:
            lista_fibonacci.append(lista[i])
orden_ascendente(lista_primos)
orden_descendente(lista_fibonacci)
print(f"la lista ingresada fue : {lista}")
print(f"la lista con los primos sin repetir y en orden ascendente es : {lista_primos}")
print(f"la lista con los fibonacci sin repetir y en orden descendente es : {lista_fibonacci}")


