from machine import Pin, ADC
import utime
import os

# --- 1. Configuración del ADC ---
# Usamos el GPIO 34 como ejemplo (puedes cambiarlo si usas otro pin ADC).
PIN_ADC = 34 
adc_pin = Pin(PIN_ADC, Pin.IN)
adc = ADC(adc_pin)

# Atenuación para medir hasta ~3.3V
adc.atten(ADC.ATTN_11DB) 

# --- 2. Variables del Archivo y del Contador ---
NOMBRE_ARCHIVO = "adc_log.csv"
LIMITE_LECTURAS = 30  # <--- Definimos el límite a 30

def leer_adc():
    """Realiza la lectura del ADC y la convierte a un valor utilizable."""
    lectura_raw = adc.read()
    voltaje = (lectura_raw / 4095.0) * 3.3
    return lectura_raw, voltaje

def obtener_datos_csv():
    """Obtiene la lectura del ADC y la formatea con fecha y hora."""
    lectura_raw, voltaje = leer_adc()
    timestamp = utime.localtime()
    
    # Formato: Fecha, Hora, Lectura_RAW, Voltaje_V
    linea_csv = "{:04d}-{:02d}-{:02d},{:02d}:{:02d}:{:02d},{:d},{:.3f}\n".format(
        timestamp[0], timestamp[1], timestamp[2],
        timestamp[3], timestamp[4], timestamp[5],
        lectura_raw,
        voltaje
    )
    return linea_csv

def guardar_csv(datos):
    """Abre el archivo y añade la nueva línea de datos."""
    try:
        # Usamos 'a' (append) para añadir al final del archivo.
        with open(NOMBRE_ARCHIVO, 'a') as archivo:
            archivo.write(datos)
        # Solo mostramos el primer segmento para no llenar la consola
        print(f"Datos guardados: {datos[:20].strip()}...") 
        
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# --- 3. Inicialización: Crear el encabezado (si no existe) ---
try:
    os.stat(NOMBRE_ARCHIVO)
except OSError:
    print(f"Creando el archivo '{NOMBRE_ARCHIVO}'...")
    encabezado = "Fecha,Hora,Lectura_RAW,Voltaje_V\n"
    guardar_csv(encabezado)

# --- 4. Bucle de Registro con Límite ---
print(f"Iniciando registro de ADC... (Máximo {LIMITE_LECTURAS} lecturas)")

contador = 0
while contador < LIMITE_LECTURAS:
    # 4.1. Generar y guardar los datos
    datos_para_guardar = obtener_datos_csv()
    guardar_csv(datos_para_guardar)
    
    # 4.2. Incrementar el contador
    contador += 1
    print(f"Lectura #{contador} de {LIMITE_LECTURAS} completada.")
    
    # 4.3. Esperar para la siguiente lectura (ej. 5 segundos)
    utime.sleep(1) 

# --- 5. Fin del Registro ---
print("\n**************************************")
print(f"¡REGISTRO COMPLETADO! {LIMITE_LECTURAS} lecturas guardadas.")
print("El ESP32 se detiene ahora.")
print("**************************************")
