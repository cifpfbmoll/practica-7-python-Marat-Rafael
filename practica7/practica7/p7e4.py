'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que pida una frase (entrada por teclado), 
y le pase como parámetro a una función dicha frase. 
La función debe sustituir todos los espacios en blanco de una frase por un asterisco, 
y devolver el resultado para que el programa principal la imprima por pantalla.
"""

def sustituirEspacios(frase):
    print (frase.replace(" ", "*"))

print ("Introduce una frase por,favor, vamos a sustituir espacios en blanco por un asterisco",end=" ")

frase=str(input())

sustituirEspacios(frase)

