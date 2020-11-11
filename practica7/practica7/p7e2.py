'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que lea (entrada por teclado) 
el nombre y los dos apellidos de una persona 
(en tres cadenas de caracteres diferentes), 
los pase como parámetros a una función, 
y ésta debe unirlos y devolver una única cadena. 
La cadena final la imprimirá el programa por pantalla.
"""

def nombreCompleto(nombre,apelido1,apelido2):
    print (" ".join([nombre.title(),apelido1.title(),apelido2.title()]))
        

nombre= input("Introduce su nombre: ")

apelido1 = input("introduce su primer apelido por favor: ")

apelido2 = input("introduce su segundo apelido por favor: ")


nombreCompleto(nombre,apelido1,apelido2)

