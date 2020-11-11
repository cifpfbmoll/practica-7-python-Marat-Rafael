'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que pida dos palabras las pase como parámetro 
a un procedimiento y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden solo las dos últimas tiene que decir que riman un poco y si no, que no riman.

"""

"""endswith (suffix[, start[, end]])
Devuelve verdadero si la cadena finaliza con el sufijo suffix especificado, 
en caso contrario falso. Si se da valor al parámetro opcional start, 
la comprobación empieza en esa posición. Si se da valor al parámetro opcional end, 
la comprobación finaliza en esa posición."""


def buscarRima(palabra1,palabra2):
   
    if palabra1[-3:]==palabra2[-3:]:
        print ("Las palabras '{0}' y '{1}' riman!" .format(palabra1,palabra2))
    elif palabra1[-2:]==palabra2[-2]:
        print ("Palabras '{0}' y '{1}' riman un poco " .format(palabra1,palabra2))
    else:
        print ("Palabras '{0}' y '{1}' NO riman ! " .format(palabra1,palabra2))
    
    
print ("Vamos a comprobar si dos palabras riman o no ! ")

palabra1=str(input("Introduce la primera palabra, por favor: "))
palabra1=palabra1.lower()

palabra2=str(input("Introduce la segunda palabra, por favor: "))
palabra2=palabra2.lower()

buscarRima(palabra1,palabra2)


