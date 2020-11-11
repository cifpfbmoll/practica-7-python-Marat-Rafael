'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que te pida una frase y una vocal (entrada por teclado), 
y pase estos datos como parámetro a una función que se encargará de cambiar todas las vocales 
de la frase por la vocal seleccionada. Devolverá la función la frase modificada, 
y el programa principal la imprimirá:
"""

def cambiarVocales(frase,letra):
    for i in frase:
        if i =="a" or i=="o" or i=="e" or i=="i" or i=="u" or i=="y":
            frase=frase.replace("a",letra)
            frase=frase.replace("e",letra)
            frase=frase.replace("i",letra)
            frase=frase.replace("o",letra)
            frase=frase.replace("u",letra)
            frase=frase.replace("y",letra)
    print (frase) 
      
      
"""        if i in vocales:
            frase=frase.replace(i,letra)
    print (frase)
    
"""

vocales="aeiouy"
print ("Escribe una frase, le cambiamos todas las vocales por lo que queres",end=" ")
frase=input()
frase.capitalize()
letra=str(input("Introduce lo que vas sustituir a todas vocales: "))
letra.lower()

cambiarVocales(frase,letra)








