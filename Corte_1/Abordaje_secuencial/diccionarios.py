# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

# print(sensors)
# print(num_cameras)
# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
# print(translations)

##Verifiying an error:
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# # print(powers)

# children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
# print(children)

# my_empty_dictionary = {}
# print(my_empty_dictionary)

# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# print("Before: ", menu)
# menu["cheesecake"] = 8
# print("After", menu)
# animals_in_zoo = {"dinosaurs": 0}
# animals_in_zoo = {"dinosaurs": 0}
# animals_in_zoo = {"horses": 2}
# print(animals_in_zoo)


##Add multiple keys
# sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
# print("Before", sensors)

# #If we wanted to add 3 new rooms, we could use:
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
# print("After", sensors)

###
# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
# print(user_ids)
# user_ids.update({"theLooper": 138475, "stringQueen": 85739})
# print(user_ids)

## Overwrite Values ##
#We know that we can add a key by using the following syntax:
#menu["banana"] = 3
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# print("Before: ", menu)
# menu["oatmeal"] = 5
# print("After", menu)

## Notice the value of "oatmeal" has now changed to 5.
# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
# print("Before", oscar_winners)
# print()
# oscar_winners.update({"Supporting Actress": "Viola Davis"})
# print("After1", oscar_winners)
# print()
# oscar_winners["Best Picture"] = "Moonlight"
# print("After2", oscar_winners)


###Dict Comprehensions
#Let’s say we have two lists that we want to combine into a 
#dictionary, like a list of students and a list of their heights, 
#in inches:
"""
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
"""
#Python allows you to create a dictionary using 
# a dict comprehension, with this syntax:

# zipStudents = zip(names, heights)
# print("zipStudents: ", zipStudents)

# students = {key:value for key, value in zip(names, heights)}
# #students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
# print(students)

# #zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:

# drinks = ["espresso", "chai", "decaf", "drip"]
# caffeine = [64, 40, 0, 120]

# zipped_drinks = zip(drinks, caffeine)
# print(zipped_drinks)

# drinks_to_caffeine = {key:value for key, value in zipped_drinks}
# print(drinks_to_caffeine)

# ==============================
# Diccionarios en Python
# ==============================

# Creamos dos listas: nombres de canciones y número de veces reproducidas
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
# zip(songs, playcounts) combina ambas listas en pares (canción, reproducciones)
# dict comprehension {clave: valor for clave, valor in zip(...)}
# genera un diccionario a partir de esos pares
plays = {key:value for key, value in zip(songs, playcounts)}
# Mostramos el diccionario plays creado
print("diccionario inicial de plays:"plays)
# Resultado esperado:
# {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44,
#  'What's Going On': 21, 'Respect': 89, 'Good Vibrations': 5}

# ======================================
# Agregar elementos a un diccionario
# ======================================

# El método .update() permite agregar un nuevo par clave:valor
plays.update({"Purple Haze": 1})
# Ahora el diccionario plays tiene una nueva canción con 1 reproducción
# {'Purple Haze': 1} fue agregado
# plays ahora tiene 7 canciones

# ======================================
# Modificar valores existentes
# ======================================

# Si usamos update() con una clave que ya existe, se sobrescribe su valor
plays.update({"Respect": 94})

# Antes 'Respect': 89
# Después 'Respect': 94
print("Despues de agregar y modificar: ", plays)
# Resultado esperado:
# {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44,
#  'What's Going On': 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}

# ======================================
# Diccionarios anidados
# ======================================

# Podemos guardar un diccionario dentro de otro
library = {"The Best Songs": plays, # Diccionario con todas las canciones y sus reproducciones
           "Sunday Feelings": {}}   # Diccionario vacío (puede llenarse más adelante)
print("Diccionario anidado (library):"library)

# ==============================
# Resumen de métodos usados
# ==============================
# 1. zip(lista1, lista2) -> une elementos en pares.
# 2. {k:v for k,v in zip(...)} -> dict comprehension para crear diccionarios.
# 3. dict.update({clave: valor}) -> agrega o modifica pares clave:valor.
# 4. Diccionarios anidados -> estructuras más complejas con diccionarios dentro de otros.
