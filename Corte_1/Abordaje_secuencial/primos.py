#9 septiembre 8-10 am, valor de una decima de corte 1 
numero = int(input("Ingresa un número: "))

# Los números menores o iguales a 1 no son primos
if numero <= 1:
    print("El número", numero, "NO es primo")

# 2 y 3 son primos
elif numero == 2 or numero == 3:
    print("El número", numero, "es primo")

# Verificamos divisibilidad
else:
    es_primo = True  
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número", numero, "es primo")
    else:
        print("El número", numero, "NO es primo")
