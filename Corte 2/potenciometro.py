import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV
# Asegúrate de que el nombre del archivo sea correcto si lo ejecutas localmente.
# En este entorno de Jupyter/Colab, ya está cargado como 'adc_log.csv'
try:
    df = pd.read_csv('adc_log.csv')
except FileNotFoundError:
    print("Error: El archivo 'adc_log.csv' no fue encontrado.")
    exit()

# 2. Preprocesamiento: Combinar 'Fecha' y 'Hora' en un único índice de tiempo
df['Tiempo'] = pd.to_datetime(df['Fecha'] + ' ' + df['Hora'])
df.set_index('Tiempo', inplace=True)

# 3. Crear la Gráfica

# Crea una figura y un conjunto de subtramas (axes)
fig, ax1 = plt.subplots(figsize=(12, 6)) # Tamaño de la figura

# Título de la Gráfica
fig.suptitle('Registro de Voltaje y Lectura RAW del ADC a lo Largo del Tiempo', fontsize=16)

# --- Eje Y principal (Izquierda) para el Voltaje ---
color = 'tab:blue'
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Voltaje (V)', color=color)
ax1.plot(df.index, df['Voltaje_V'], color=color, label='Voltaje (V)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.6) # Añadir rejilla al eje principal

# --- Eje Y secundario (Derecha) para la Lectura RAW ---
ax2 = ax1.twinx() # Crea un segundo eje Y que comparte el mismo eje X
color = 'tab:red'
ax2.set_ylabel('Lectura RAW', color=color)
ax2.plot(df.index, df['Lectura_RAW'], color=color, linestyle='--', alpha=0.7, label='Lectura RAW')
ax2.tick_params(axis='y', labelcolor=color)

# 4. Mejorar la visualización
# Rotar etiquetas del eje X para mejor lectura
fig.autofmt_xdate(rotation=45)

# Añadir una leyenda combinada para ambos ejes (puede requerir un pequeño ajuste)
# Para simplificar, añadiremos la leyenda directamente en los ejes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right')

# Mostrar la gráfica
plt.show()

print("\nGráfica generada con éxito.")
print("Muestra las series de 'Voltaje_V' (eje izquierdo) y 'Lectura_RAW' (eje derecho) en función del tiempo.")
