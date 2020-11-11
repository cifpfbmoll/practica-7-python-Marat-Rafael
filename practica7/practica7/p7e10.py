'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribe un programa que te pida una palabra o número, 
pase por parámetro estos datos a una función, y ésta te diga si es o no palíndroma o capicúa. 
El programa principal imprimirá el resultado de la función:"""

def comprobarPolindrom(entrada):
    
    entrada1=entrada.strip()           #elimina espacios y tabs  al principio i final
    entrada2=entrada1.replace(" ","")  #elimina resto del espacios
    print ("texto sin espacios en blanco y tabuladores: ",entrada2)
    if entrada2 == entrada2[:: -1]:    #lea entrada y lea entrada del atravez

        print ("polindrom") 
    else:
        print ("no es polindrom")
             

print("Vamos a comprobar si una palabra o numero es palindroma!")

entrada=str(input("Introduce palabra o numero: "))


comprobarPolindrom(entrada)

