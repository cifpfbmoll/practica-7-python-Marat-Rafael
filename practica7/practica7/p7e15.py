'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''


"""Desarrolla un programa utilizando la metodología “pair programming”, 
que nos sirva para gestionar nuestros contactos 
(la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico. 
El programa tendrá un menú, con las siguientes opciones: 
añadir contacto, consultar contacto a partir de la clave, consultar todos los contactos y eliminar contacto. 
Aprovecha lo que has aprendido hasta el momento (diccionarios, funciones, procedimientos…).

"""
#declaramos diccionario para manejar contactos
libreta={
    "Alex": [" Baskota " " Arenal " " 971 99 88 77 " " alex@gmail.com "],
    "Josep": [" System " " Master " " 314 15 92 6 " " sudoaptget@update.es "],
    "James" : [" Bond " "Bond" " 007 007 007 " " agente007@estoyocupado.ru "],
    "Aaron" : [" Delegado " " uib " " 999 888 777 " " delegado@dam.es "]
    } 

def menuContactos():
    consultando=True
    print ("----------------------------------")
    print ("<<< Bienvenido a libro de contactos ! >>>")
    print ("----------------------------------")
    print (" 1 : Añadir")
    print (" 2 : Consultar ")
    print (" 3 : Ver todo ")
    print (" 4 : Modificar ")
    print (" 5 : Borrar ")
    print (" 0 : Salir ")
    print ("----------------------------------")
    
    opcion=""
    opcion=input()
    if opcion=="1":
        añadirContacto()
    elif opcion=="2":
        consultarContacto()
    elif opcion=="3":
        verTodo()
    elif opcion=="4":
        modificarContacto()
    elif opcion=="5":
        borrarContacto()
    elif opcion=="0":
        consultando=False


def borrarContacto():
    nombre=input()
    if nombre not in libreta:
        print ("Este nombre no existe")
    else:
        del libreta[nombre]
        print ("El contacto se ha borrado correctomente")
    menuContactos()
            

def modificarContacto():
    nombre=input("Nombre: ")
    if nombre not in libreta:
        print ("Este nombre no esta en la libreta")
    else:
        print ("Primer apellido: ",end=" ")
        apellido1=str(input())
        print ("Segundo apellido: ",end=" ")
        apellido2=str(input())
        print ("su telefono:",end=" ")
        telefono=int(input())
        print ("correo electronico: ",end=" ")
        correo=str(input())
        libreta[nombre]= [apellido1,apellido2,telefono,correo]
        print ("Nombre '{0}' modificado corectamente " )
    menuContactos()    
        
def verTodo():
    for i in libreta:
        print (i,":",libreta[i])
        
    #print (libreta)
    menuContactos()
    
def añadirContacto():
    
    print ("Escribe nombre por favor (debe ser unico) ",end=" "  )
    nombre=str(input())  
    print ("Primer apellido: ",end=" ")
    apellido1=str(input())
    print ("Segundo apellido: ",end=" ")
    apellido2=str(input())
    print ("su telefono:",end=" ")
    telefono=int(input())
    print ("correo electronico: ",end=" ")
    correo=str(input())
    libreta[nombre] = [apellido1,apellido2,telefono,correo]
    #print (libreta)
    
    menuContactos()
    
def consultarContacto():
    print ("Escribe nombre del contacto que desea consultar: ",end=" ")
    consulta=str(input())
  
    if consulta not in libreta:
        print ("Este nombre no existe")
    else:
        print (" {0} : ".format(consulta),(libreta[consulta]) )
    menuContactos()

    
menuContactos()





