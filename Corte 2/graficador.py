import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Configuración ---
NOMBRE_ARCHIVO_CSV = 'numeros_aleatorios.csv'
COLUMNA_VALOR = 'Numero_Aleatorio' # Debe coincidir con la cabecera del otro script

def graficar_numeros_csv(nombre_archivo=NOMBRE_ARCHIVO_CSV, nombre_columna=COLUMNA_VALOR):
    """
    Lee los números de un archivo CSV en la misma carpeta y los grafica:
    Número (valor) contra Orden (índice).
    """
    print(f"\n--- 📈 Iniciando graficación de '{nombre_archivo}' ---")
    
    # 1. Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"❌ Error: No se encontró el archivo '{nombre_archivo}' en la carpeta actual.")
        print("Asegúrate de ejecutar primero el script de generación para crear el CSV.")
        return

    try:
        # 2. Leer el archivo CSV usando pandas
        df = pd.read_csv(nombre_archivo)
        
        # 3. Validar y obtener los datos
        if nombre_columna not in df.columns:
            print(f"❌ Error: La columna '{nombre_columna}' no se encontró en el archivo.")
            print(f"Columnas disponibles: {list(df.columns)}")
            return

        numeros = df[nombre_columna].tolist()
        
        if not numeros:
            print("❌ Error: El archivo CSV está vacío o la columna no contiene datos.")
            return

    except pd.errors.EmptyDataError:
        print(f"❌ Error: El archivo '{nombre_archivo}' está vacío.")
        return
    except Exception as e:
        print(f"❌ Ocurrió un error al leer el archivo: {e}")
        return

    # 4. Preparar los datos para la gráfica
    y_valores = numeros
    # El eje X es el 'orden' o 'índice'.
    x_orden = list(range(len(y_valores)))
    
    # 5. Crear la gráfica 
    plt.figure(figsize=(12, 6))
    
    # Gráfica de línea y puntos
    plt.plot(x_orden, y_valores, marker='o', linestyle='-', color='teal', 
             label='Número vs. Orden', markersize=3, linewidth=1, alpha=0.7)
    
    # 6. Configurar los títulos y etiquetas
    plt.title(f'Gráfico de Valores Aleatorios (N={len(y_valores)})', fontsize=16, weight='bold')
    plt.xlabel('Orden / Índice (Posición)', fontsize=12)
    plt.ylabel('Valor del Número (entre 0 y 1)', fontsize=12)
    
    # Ajustes visuales
    plt.ylim(0, 1) # Asegura el rango de 0 a 1
    plt.axhline(y=0.5, color='red', linestyle='--', linewidth=1, alpha=0.6, label='Referencia 0.5')
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # 7. Mostrar la gráfica
    plt.show()

# Ejecutar la función de graficación
if __name__ == "__main__":
    # Asegúrate de tener instaladas las librerías: pip install pandas matplotlib
    graficar_numeros_csv()
