#9 septiembre 8-10 am, valor de una decima de corte 1 
# Pedir un número al usuario

while True:
    try:
        numero = int(input("Ingresa un número: "))
        if numero % 2 ==0:
          print("El número", numero, "es PAR")
        else:
          print("El número", numero, "es IMPAR")

    except ValueError:
       print("Error, ingrese un numero entero")
    except KeyboardInterrupt:
       print("\n el programa ha finalizado, gracias")
     
# Verificar el residuo al dividir entre 2


