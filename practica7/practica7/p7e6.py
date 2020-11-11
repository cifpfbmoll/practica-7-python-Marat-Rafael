'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que lea el nombre de una persona y un carácter (entrada por teclado), 
le pase estos datos a una función que comprobará si dicho carácter está en su nombre. 
El resultado de dicha función lo imprimirá el programa principal por pantalla.
"""
def comprobarCaracter(nombre,caracter):
    presente=True
    for i in nombre:
        if caracter == i:
            presente=True           
        else:
            presente=False
    if presente == True:
        print (("caracter '{0}' esta presente en el nombre '{1}' ".format(caracter,nombre)))
    else:
        print (("caracter '{0}' NO esta presente en el nombre '{1}' ".format(caracter,nombre)))
        
print ("Inroduce un nombre y un caracter, para ver si esta presente en este nombre ")
nombre=str(input("Introduce un nombre: "))
caracter=str(input("Introduce un caracter: "))

comprobarCaracter(nombre, caracter)

