#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']#se crea una lista llamada my_lista
#input()
print(my_lista)#se imprime la lista creada 
print(type(my_lista))
print(my_lista[2])# se imprieme el elemento de la posicion dos de la lista, el cujal sera amarillo porque se empieza desde 0

print("my_lista size: ", len(my_lista))#imprime la cantidad de elementos que tenga la lista en este caso sera 6
print(my_lista[0:2])#imprime una seccion de la lista hasta 2, incluyendo 0 y 1 
print(my_lista[:2])#es igual a la linea anterior solo que se omite el el 0:2 y se deja solo :2

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista)#imprime la lista despues de agregar el nuevo elemento 

my_lista.insert(3, 'Negro')#inserta en la posicion 3 de la lista el nuevo elemento, teniendo en cuenta que se inicia desde 0
print(my_lista)#imprime la lista despues de agregar el nuevo elemento 


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)#imprime la lista despues de agregar el nuevo elemento 

print(my_lista.index('Azul'))#busca el valor del elemento igual a azul en este caso 1 por su posicion y lo imprime 


my_lista.remove('Marron')#remueve el primer elemento que sea marron 
print(my_lista)#imprime la lista despues de remover el elemento 

my_lista.insert(8, 'Marron')#agrega el elemento marron a la lista en la posicion 8
print(my_lista)#imprime la lista despues de agregar el nuevo elemento 

print(my_lista.pop())#elimina y emprime el ultimo elemento de la lista 
size = len(my_lista)#guarda el tamaño actual de la lista
print("size = ", size)#imprime el tamaño de la lista 
#print(my_lista.pop(size))

my_lista_3 = my_lista*3#multiplica la lista por tres, lo que quiere decir que los elementos de la lista se repiten 3 veces 
print("my_lista_3: ", my_lista_3)#imprime la lista despues de multiplicar los elementos 

print("Sort:")#imprime la palabra sort
print()#imprme nada
my_listaSort = my_lista.sort()#Ordena la lista my_lista en orden ascendente. sort() modifica la lista en su lugar y retorna None
print(my_listaSort)#imprime la lista my_listaSort

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]#crea una lista 
print("Ordering my_NumList: ")#indica que se van a ordenar los numeros  
my_NumList.sort()#ordena la lista en orden ascendente 
print(my_NumList)#imprime la lista en orden 
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)#orden la lista de mayor a menor 
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)#Convierte la lista my_lista a una tupla y la asigna a la variable my_tupla
print()
print()
print("my_tuple: ", my_tupla)#imprime la lista completa 

print(my_tupla[0])#Imprime el elemento en la posición 0 de la lista
print(my_tupla[2])#Imprime el elemento en la posición 2 de la lista

#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)#Verifica si 'Rojo' está presente en la tupla.
print(my_tupla.count('Rojo'))#cuenta cuántas veces aparece 'Rojo' en la tupla.

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')#crea una tupla con un solo elemento
print(my_tupla_unitaria)#imprime la tupla 

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999#crea una tupla sin parentesis, a lo que se le llama empaquetado
print(my_tupla)#imprime la tupla  

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
