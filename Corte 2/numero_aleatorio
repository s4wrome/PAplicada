import random
import csv
import os

# --- Configuración ---
NOMBRE_ARCHIVO_DEFECTO = "numeros_aleatorios.csv"
COLUMNA_VALOR = 'Numero_Aleatorio' # Nombre de la cabecera

def generar_y_guardar_aleatorios(n, nombre_archivo=NOMBRE_ARCHIVO_DEFECTO):
    """
    Genera 'n' números aleatorios de punto flotante en el rango (0, 1)
    (excluyendo 0 y 1) y los guarda en un archivo CSV.
    """
    if not isinstance(n, int) or n <= 0:
        print("⚠️ Error: La cantidad de números 'n' debe ser un entero positivo.")
        return False

    # Límites para asegurar la exclusión estricta de 0 y 1
    min_val = 1e-9
    max_val = 1 - 1e-9
    
    # 1. Generar los números aleatorios
    numeros_aleatorios = [random.uniform(min_val, max_val) for _ in range(n)]

    # 2. Guardar los números en el archivo CSV
    try:
        # Abre el archivo en modo escritura ('w') sin espacios extra entre líneas (newline='')
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)

            # Escribir la cabecera
            escritor_csv.writerow([COLUMNA_VALOR])

            # Escribir cada número como una fila
            for numero in numeros_aleatorios:
                escritor_csv.writerow([numero])

        # Obtener la ruta completa para mostrar al usuario
        ruta_completa = os.path.abspath(nombre_archivo)
        print(f"\n✅ ¡Éxito! Se han generado y guardado *{n}* números aleatorios en:")
        print(f"    {ruta_completa}")
        print("    Los números generados están en el rango (0, 1) estricto.")
        return True

    except IOError as e:
        print(f"❌ Error al escribir en el archivo CSV: {e}")
        return False

# --- Función Principal para Interacción con el Usuario ---
def main():
    """
    Pide al usuario la cantidad de números y llama a la función de generación.
    """
    print("\n" + "="*50)
    print("✨ GENERADOR DE CSV DE NÚMEROS ALEATORIOS ✨")
    print("="*50)
    
    while True:
        try:
            # Pedir al usuario la cantidad de números
            entrada = input("¿Cuántos números aleatorios desea generar (entre 0 y 1)? Ingrese un número entero (0 para salir): ")
            
            # Convertir la entrada a entero
            N_NUMEROS = int(entrada)
            
            # Validar que sea positivo
            if N_NUMEROS == 0:
                print("Programa de generación finalizado.")
                return
            elif N_NUMEROS > 0:
                break
            else:
                print("Por favor, ingrese un número entero positivo o 0 para salir.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese solo un número entero.")

    # Llama a la función principal con la cantidad ingresada
    generar_y_guardar_aleatorios(N_NUMEROS)

# Ejecutar el programa
if __name__ == "__main__":
    main()
