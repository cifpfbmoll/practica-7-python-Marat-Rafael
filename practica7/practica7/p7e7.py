'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que lea una frase (entrada por teclado), 
y la pase como parámetro a un procedimiento. 
El procedimiento contará el número de vocales (de cada una) que aparecen, 
y lo imprimirá por pantalla.
"""

def contarVocales(frase):
    count=int(0)
    listaVocales=["a","o","i","e","u","y"]
    
    """
    for i in frase:
        if i == "a" or i=="o" or i == "i" or i=="e" or i=="y" or i =="u":
            count+=1
    print  ("el numero de vocales en la frase '{0}' es: {1} ".format(frase,count))    
            """          
            
    for i in frase:
        if i in listaVocales:
            count+=1
    print  ("el numero de vocales en la frase '{0}' es: {1} ".format(frase,count))    

print("Vamos a contar los vocales de una frase ")

frase=str(input("Introduce una frase: "))


contarVocales(frase)
