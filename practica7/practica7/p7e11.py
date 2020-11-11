'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''
"""Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. 
Ésta debe devolver si es palíndroma o no, y el programa principal escribirá el resultado por pantalla:"""

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


