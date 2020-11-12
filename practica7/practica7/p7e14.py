'''
11 nov. 2020

author: Marat-Rafael

DAM1        
2020-2021
CIFP Borja Moll

'''

"""Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento, 
que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes. 
Comentario: no es necesario validar si la es correcta, damos por hecho que lo será.
 
dicionario = {“Love Actually “: “Richard Curtis”,
    “Kill Bill”: “Tarantino”,
    “Amélie”: “Jean-Pierre Jeunet”}
    
dicionario.get(key, default=None)
Devuelve el valor del elemento con clave key. Sino devuelve default


"""
dicionario={"01": "enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"deciembre"}
def mostrarMes():
    print ("Introduce la fecha en formato 'dd/mm/aaaa' (por ejemplo: 05/07/2077) ")
    fecha=input()
    fecha=fecha.strip()           #elimina espacios y tabs  al principio i final
    fecha=fecha.replace(" ","")   #elimina espacios si hay en medio
    fecha=fecha.replace("/","")   #elimina barra
    dia=fecha[0]+fecha[1]
    mes=fecha[2]+fecha[3]
    mes_escrito=dicionario.get(mes)    
    año=fecha[4]+fecha[5]+fecha[6]+fecha[7]
    #print (mes)
    #print (mes_escrito)
    #print (fecha)
    print ("La fecha indicada es {0} de {1} de {2} ".format(dia,mes_escrito,año))
    
    
    
mostrarMes()


    
