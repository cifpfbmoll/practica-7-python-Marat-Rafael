'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''
"""Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, 
por tanto, habrá dos funciones que se caracterizan por hacer ese mismo cálculo de una manera 
(con for y sin breaks), o de otra (con while). 
Ambas funciones devolverá true (si es primo) o false (si no es primo). 
El programa principal informará del resultado. Además, 
como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra. 
Comentario: aprovecha el código que tienes ya creado

"""

def bucleFor():
    print ("Introduce un numero para ver si es primo: ")
    numero=int(input())
    
    #es numero mayor que uno y se divide solo a si misno y uno
    primo=True    
    contador=int(0)    
    for i in range (1,numero+1): 
        resto=numero%i       
        if resto == 0:            
            contador+=1                        
    if contador == 2: # se divide en uno y numero mismo       
        primo=True
        print ("El numero '{0}' es un numero primo" .format(numero))
    else:
        primo=False
        print ("El numero '{0}' NO es un numero primo" .format(numero))
        
def bucleWhile():
    print ("Introduce numero para comprobar si es primo: ")
    numero=int(input())
    #es numero mayor que uno y se divide solo a si misno y uno
    contador=int(0)
    for i in range (1,numero+1): 
        while i<numero and contador==0:
            resto=numero%i
            if resto==0:
                contador+=1
                if contador > 2: # se divide en uno y numero mismo
                    print ("El numero '{0}' NO es un numero primo" .format(numero))   
                else:
                    print ("El numero '{0}' es un numero primo" .format(numero))

def eligirBucle():
    print ("Para ver si un numero primo podemos usar bucles 'FOR' o 'WHILE' ")
    print ("****************************************************************")
    print ("Elige !")
    print ("****************************************************************")
    print ("Si deseas usar bucle 'FOR' ")
    print ("introduce 1")
    print ("****************************************************************")
    print ("Si desea usar bucle 'WHILE' ")
    print ("introduce 2")
    print ("****************************************************************")
    print ("Eliges tu !!!")
    bucle=int(input())
    print ("****************************************************************")
    while bucle > 2:
        print ("1 para usar bucle FOR , 2 para usar bucle WHILE, prueba otra vez , tu puedes !")
        bucle=int(input())
        
    if bucle==1:
        print ("Has eligido bucle 'for' ! ")
        print ("**********************FOR***************************************")
        bucleFor()
                
    elif bucle==2:
        print ("Has eligido bucle 'while' !")
        print ("*******************WHILE****************************************")
        bucleWhile()
            
        
eligirBucle()

