'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Escribir un programa que lea una frase, 
y pase ésta como parámetro a una función que debe contar el número de palabras que contiene. 
Debe imprimir el programa principal el resultado. Asumir que cada palabra está separada por un solo blanco:
Asumir que cada palabra está separada por un solo blanco.
No se sabe cómo están separadas las palabras. 
Pueden estar separadas por más de un blanco o por signos de puntuación.

"""

"""
textos para probar:
¿Acaso hubo búhos acá?
A la catalana banal, atácala.
A mamá, Roma le aviva el amor a papá y a papá, Roma le aviva el amor a Mamá.
Arriba la birra.
A ti no, bonita.
Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida
Ají traga la lagartija
Allí por la tropa portado, traído a ese paraje de maniobras, una tipa como capitán usar boina me dejara, pese a odiar toda tropa por tal ropilla 
"""
def comprobarPolindrom(entrada):
    
    entrada1=entrada.strip()           #elimina espacios y tabs  al principio i final
    entrada2=entrada1.replace(" ","")  #elimina resto del espacios
    entrada3=entrada2.replace(",","")  #eliminar comas
    entrada4=entrada3.replace(".","")  #eliminar puntos
    entrada5=entrada4.replace("á","a") #eliminar acentos 'a'
    entrada6=entrada5.replace("í","i") #eliminar acentos 'i'
    entrada7=entrada6.replace("é","e") #eliminar acentos 'e'
    entrada8=entrada7.replace("ó","o") #eliminar acentos 'o'
    entrada9=entrada8.replace("ú","u") #eliminar acentos 'u'
    entrada10=entrada9.replace("?","")
    entrada11=entrada10.replace("¿","")
    
    entrada12=entrada11.lower()
    
    print ("texto sin espacios en blanco y tabuladores y acentos: ",entrada12)
    if entrada12 == entrada12[:: -1]:    #lea entrada y lea entrada del atravez

        print ("polindrom") 
    else:
        print ("no es polindrom")
             

print("Vamos a comprobar si una palabra o numero es palindroma!")

entrada=str(input("Introduce palabra o numero: "))

comprobarPolindrom(entrada)

