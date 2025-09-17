# Definición de un diccionario con alturas de algunos rascacielos.
building_heights = {
    "Burj Khalifa": 828,  # Altura en metros
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Ejemplo de acceso al valor de una clave:
print(building_heights["Burj Khalifa"])  # Imprime: 828
print(building_heights["Ping An"])  # Imprime: 599

# Definición de un diccionario con los elementos del zodiaco.
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],  # Elemento agua con los signos correspondientes
    "fire": ["Aries", "Leo", "Sagittarius"],  # Elemento fuego
    "earth": ["Taurus", "Virgo", "Capricorn"],  # Elemento tierra
    "air": ["Gemini", "Libra", "Aquarius"]  # Elemento aire
}

# Acceso a los valores de los elementos del zodiaco.
print(zodiac_elements["earth"])  # Imprime: ["Taurus", "Virgo", "Capricorn"]
print(zodiac_elements["fire"])  # Imprime: ["Aries", "Leo", "Sagittarius"]

# Acceso a una clave que no existe, lo cual genera un error.
# Esto genera un error ya que "Landmark 81" no es una clave en `building_heights`.
# print(building_heights["Landmark 81"])

# Alternativa para evitar errores:
# Usamos `in` para comprobar si la clave existe antes de acceder a ella.
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])  # Esto no se ejecutará ya que la clave no existe.

# Se añade una nueva clave al diccionario zodiac_elements.
zodiac_elements["energy"] = "Not a Zodiac element"

# Comprobamos si la clave 'energy' está en el diccionario.
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])  # Imprime: "Not a Zodiac element"

# Acceso seguro a claves con `.get()`, lo que evita errores si la clave no existe.
# Este método devuelve `None` si la clave no se encuentra.
print(building_heights.get("Shanghai Tower"))  # Imprime: 632
print(building_heights.get("My House"))  # Imprime: None

# Uso de `.get()` con una estructura condicional.
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# Si el usuario no existe en el diccionario, se asigna un valor predeterminado.
tc_id = user_ids.get("teraCoder", 1000)
print(tc_id)  # Imprime: 100019, ya que "teraCoder" existe en el diccionario.

# Para un usuario inexistente, asignamos un ID predeterminado.
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)  # Imprime: 100000

# El método `.pop()` elimina una clave de un diccionario y devuelve su valor.
raffle = {
    223842: "Teddy Bear", 
    872921: "Concert Tickets", 
    320291: "Gift Basket", 
    412123: "Necklace", 
    298787: "Pasta Maker"
}
print(raffle.pop(320291, "No Prize"))  # Imprime: "Gift Basket"
print(raffle)  # Imprime: {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}

# Si intentamos eliminar una clave que no existe, podemos especificar un valor predeterminado.
print(raffle.pop(100000, "No Prize"))  # Imprime: "No Prize"
print(raffle)  # Imprime: {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}

# Se eliminan otras claves del diccionario.
print(raffle.pop(872921, "No Prize"))  # Imprime: "Concert Tickets"
print(raffle)  # Imprime: {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

# Se añaden valores a `health_points` desde el diccionario `available_items`.
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}
health_points = 20

# Sumar los valores de los elementos consumidos.
health_points += available_items.pop("stamina grains", 0)  # Se suma 15 a health_points
health_points += available_items.pop("power stew", 0)  # Se suma 30 a health_points
health_points += available_items.pop("mystic bread", 0)  # No existe, por lo que se suma 0

# Imprime el estado actualizado de los elementos y los puntos de salud.
print(available_items)  # Imprime los elementos restantes
print(health_points)  # Imprime los puntos de salud actualizados

# Obtener todas las claves de un diccionario y recorrerlas.
test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}

# Obtener las claves del diccionario (nombres de los estudiantes).
print(list(test_scores))  # Imprime las claves: ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

# Recorrer las claves y mostrar el nombre de cada estudiante.
for student in test_scores.keys():
    print(student)

# Definición de un diccionario con el número de ejercicios de distintos temas.
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# Obtener las claves de `num_exercises` (temas).
users = user_ids.keys()
lessons = num_exercises.keys()

# Mostrar las claves de ambos diccionarios.
print(users)  # Muestra los usuarios
print(lessons)  # Muestra los temas

# Obtener todos los valores de un diccionario y recorrerlos.
for score_list in test_scores.values():
    print(score_list)

# Calcular el total de ejercicios sumando todos los valores del diccionario `num_exercises`.
total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)  # Imprime la suma total de los ejercicios

# Obtener todos los elementos (clave, valor) del diccionario y recorrerlos.
biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")

# Imprimir el porcentaje de mujeres en distintas ocupaciones.
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
