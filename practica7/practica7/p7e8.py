'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que pida una frase (entrada por teclado), 
y pase la frase como parámetro a una función que debe eliminar los espacios en blanco 
(compactar la frase). El programa principal imprimirá por pantalla el resultado final.

"""

def eliminarEspacio(frase):
    frase=frase.replace(" ","")
    print (frase)
    #frase=frase.strip()
    
print ("Vamos a eliminar espacios en blanco para compactar frase")

frase=str(input("Introduca la frase, por favor: "))

eliminarEspacio(frase)

